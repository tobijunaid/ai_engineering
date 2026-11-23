from decimal import Decimal

import pytest
from sqlalchemy import select

from app.models import InventoryMovement, Payment, User

INVOICES_URL = "/api/v1/invoices"


# --- setup helpers ------------------------------------------------------------

def create_product(client, headers, name, sku, price, stock):
    product_id = client.post(
        "/api/v1/products",
        json={"name": name, "sku": sku, "selling_price": price},
        headers=headers,
    ).json()["id"]
    if stock:
        client.post(
            f"/api/v1/inventory/{product_id}/movements",
            json={"movement_type": "stock_in", "quantity": stock},
            headers=headers,
        )
    return product_id


def stock_of(client, headers, product_id):
    return client.get(f"/api/v1/inventory/{product_id}", headers=headers).json()["quantity"]


@pytest.fixture
def shop(client, owner_headers):
    """A business with one customer and two stocked products."""
    customer_id = client.post(
        "/api/v1/customers", json={"full_name": "Adaeze Okafor"}, headers=owner_headers
    ).json()["id"]
    return {
        "customer": customer_id,
        "rice": create_product(client, owner_headers, "Rice 50kg", "RICE-50", "45000.00", stock=10),
        "oil": create_product(client, owner_headers, "Palm Oil 5L", "OIL-5", "8500.50", stock=4),
    }


def create_invoice(client, headers, shop, items=None):
    items = items if items is not None else [
        {"product_id": shop["rice"], "quantity": 2},
        {"product_id": shop["oil"], "quantity": 3},
    ]
    response = client.post(
        INVOICES_URL, json={"customer_id": shop["customer"], "items": items}, headers=headers
    )
    assert response.status_code == 201, response.json()
    return response.json()


def confirm(client, headers, invoice):
    return client.post(f"{INVOICES_URL}/{invoice['id']}/confirm", headers=headers)


def void(client, headers, invoice, reason="Customer cancelled order"):
    return client.post(f"{INVOICES_URL}/{invoice['id']}/void", json={"reason": reason}, headers=headers)


# --- drafts -----------------------------------------------------------------

def test_create_draft_invoice_calculates_totals(client, owner_headers, shop):
    invoice = create_invoice(client, owner_headers, shop)

    assert invoice["status"] == "draft"
    assert invoice["payment_status"] == "unpaid"
    assert invoice["invoice_number"] == "INV-00001"
    assert len(invoice["items"]) == 2
    # 2 x 45000.00 + 3 x 8500.50 = 90000.00 + 25501.50
    assert Decimal(invoice["subtotal"]) == Decimal("115501.50")
    assert Decimal(invoice["total"]) == Decimal("115501.50")


def test_draft_does_not_reduce_stock(client, owner_headers, shop):
    create_invoice(client, owner_headers, shop)
    assert stock_of(client, owner_headers, shop["rice"]) == 10  # rule 6.1


def test_invoice_numbers_increment_per_business(client, owner_headers, other_owner_headers, shop):
    assert create_invoice(client, owner_headers, shop)["invoice_number"] == "INV-00001"
    assert create_invoice(client, owner_headers, shop)["invoice_number"] == "INV-00002"

    # A different business starts its own sequence.
    rival_customer = client.post(
        "/api/v1/customers", json={"full_name": "Rival Customer"}, headers=other_owner_headers
    ).json()["id"]
    response = client.post(
        INVOICES_URL, json={"customer_id": rival_customer}, headers=other_owner_headers
    )
    assert response.json()["invoice_number"] == "INV-00001"


def test_item_snapshots_name_and_price(client, owner_headers, shop):
    invoice = create_invoice(client, owner_headers, shop, items=[{"product_id": shop["rice"], "quantity": 1}])
    client.patch(
        f"/api/v1/products/{shop['rice']}",
        json={"name": "Renamed Rice", "selling_price": "99999.00"},
        headers=owner_headers,
    )
    item = client.get(f"{INVOICES_URL}/{invoice['id']}", headers=owner_headers).json()["items"][0]
    assert item["product_name"] == "Rice 50kg"
    assert item["unit_price"] == "45000.00"


def test_add_same_product_twice_merges_line(client, owner_headers, shop):
    invoice = create_invoice(client, owner_headers, shop, items=[{"product_id": shop["rice"], "quantity": 1}])
    response = client.post(
        f"{INVOICES_URL}/{invoice['id']}/items",
        json={"product_id": shop["rice"], "quantity": 2},
        headers=owner_headers,
    )
    assert response.status_code == 200
    items = response.json()["items"]
    assert len(items) == 1 and items[0]["quantity"] == 3
    assert response.json()["subtotal"] == "135000.00"


def test_update_and_remove_draft_items(client, owner_headers, shop):
    invoice = create_invoice(client, owner_headers, shop)
    rice_item = next(i for i in invoice["items"] if i["product_id"] == shop["rice"])
    oil_item = next(i for i in invoice["items"] if i["product_id"] == shop["oil"])

    response = client.patch(
        f"{INVOICES_URL}/{invoice['id']}/items/{rice_item['id']}",
        json={"quantity": 1}, headers=owner_headers,
    )
    assert response.json()["subtotal"] == "70501.50"  # 45000 + 25501.50

    response = client.delete(f"{INVOICES_URL}/{invoice['id']}/items/{oil_item['id']}", headers=owner_headers)
    assert len(response.json()["items"]) == 1
    assert response.json()["subtotal"] == "45000.00"


def test_cannot_add_inactive_product(client, owner_headers, shop):
    client.patch(f"/api/v1/products/{shop['oil']}/deactivate", headers=owner_headers)
    response = client.post(
        INVOICES_URL,
        json={"customer_id": shop["customer"], "items": [{"product_id": shop["oil"], "quantity": 1}]},
        headers=owner_headers,
    )
    assert response.status_code == 409


# --- confirm ------------------------------------------------------------------

def test_confirm_reduces_stock_and_records_sales(client, owner_headers, shop, db_session):
    invoice = create_invoice(client, owner_headers, shop)
    response = confirm(client, owner_headers, invoice)

    assert response.status_code == 200
    assert response.json()["status"] == "confirmed"
    assert response.json()["confirmed_at"] is not None
    assert stock_of(client, owner_headers, shop["rice"]) == 8
    assert stock_of(client, owner_headers, shop["oil"]) == 1

    sales = db_session.scalars(
        select(InventoryMovement).where(InventoryMovement.reference_id == invoice["id"])
    ).all()
    assert {(m.movement_type, m.quantity) for m in sales} == {("sale", 2), ("sale", 3)}


def test_staff_can_create_and_confirm(client, staff_headers, shop):
    invoice = create_invoice(client, staff_headers, shop)
    assert confirm(client, staff_headers, invoice).status_code == 200


def test_confirm_with_insufficient_stock_changes_nothing(client, owner_headers, shop):
    # Rice is fine (2 of 10) but oil is short (5 of 4): the WHOLE confirm must fail.
    invoice = create_invoice(client, owner_headers, shop, items=[
        {"product_id": shop["rice"], "quantity": 2},
        {"product_id": shop["oil"], "quantity": 5},
    ])
    response = confirm(client, owner_headers, invoice)

    assert response.status_code == 409
    assert "Insufficient stock" in response.json()["detail"]
    assert stock_of(client, owner_headers, shop["rice"]) == 10  # rolled back too
    assert client.get(f"{INVOICES_URL}/{invoice['id']}", headers=owner_headers).json()["status"] == "draft"


def test_cannot_confirm_empty_invoice(client, owner_headers, shop):
    invoice = create_invoice(client, owner_headers, shop, items=[])
    assert confirm(client, owner_headers, invoice).status_code == 409


def test_confirmed_invoice_cannot_be_edited_or_reconfirmed(client, owner_headers, shop):
    invoice = create_invoice(client, owner_headers, shop)
    confirm(client, owner_headers, invoice)
    item_id = invoice["items"][0]["id"]

    assert client.post(
        f"{INVOICES_URL}/{invoice['id']}/items",
        json={"product_id": shop["rice"], "quantity": 1}, headers=owner_headers,
    ).status_code == 409
    assert client.patch(
        f"{INVOICES_URL}/{invoice['id']}/items/{item_id}", json={"quantity": 9}, headers=owner_headers
    ).status_code == 409
    assert client.delete(f"{INVOICES_URL}/{invoice['id']}/items/{item_id}", headers=owner_headers).status_code == 409
    assert confirm(client, owner_headers, invoice).status_code == 409
    assert stock_of(client, owner_headers, shop["rice"]) == 8  # deducted once only


# --- void -------------------------------------------------------------------

def test_void_confirmed_invoice_restores_stock(client, owner_headers, shop, db_session):
    invoice = create_invoice(client, owner_headers, shop)
    confirm(client, owner_headers, invoice)
    response = void(client, owner_headers, invoice, reason="Wrong quantities")

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "void"
    assert body["void_reason"] == "Wrong quantities"
    assert body["voided_at"] is not None and body["voided_by"] is not None
    assert stock_of(client, owner_headers, shop["rice"]) == 10
    assert stock_of(client, owner_headers, shop["oil"]) == 4

    reversals = db_session.scalars(
        select(InventoryMovement).where(
            InventoryMovement.reference_id == invoice["id"],
            InventoryMovement.movement_type == "void_reversal",
        )
    ).all()
    assert len(reversals) == 2


def test_void_draft_does_not_change_stock(client, owner_headers, shop):
    invoice = create_invoice(client, owner_headers, shop)
    assert void(client, owner_headers, invoice).json()["status"] == "void"
    assert stock_of(client, owner_headers, shop["rice"]) == 10


def test_void_requires_reason(client, owner_headers, shop):
    invoice = create_invoice(client, owner_headers, shop)
    response = client.post(f"{INVOICES_URL}/{invoice['id']}/void", json={}, headers=owner_headers)
    assert response.status_code == 422


def test_cannot_void_twice(client, owner_headers, shop):
    invoice = create_invoice(client, owner_headers, shop)
    confirm(client, owner_headers, invoice)
    void(client, owner_headers, invoice)

    assert void(client, owner_headers, invoice).status_code == 409
    assert confirm(client, owner_headers, invoice).status_code == 409
    assert stock_of(client, owner_headers, shop["rice"]) == 10  # restored once only


def test_staff_cannot_void(client, owner_headers, staff_headers, shop):
    invoice = create_invoice(client, owner_headers, shop)
    assert void(client, staff_headers, invoice).status_code == 403


def test_cannot_void_invoice_with_payments(client, owner_headers, shop, db_session):
    invoice = create_invoice(client, owner_headers, shop)
    confirm(client, owner_headers, invoice)

    # The payments module doesn't exist yet, so insert a payment row directly.
    owner = db_session.scalar(select(User).where(User.email == "owner@example.com"))
    db_session.add(Payment(
        invoice_id=invoice["id"], amount=Decimal("1000.00"),
        payment_method="cash", recorded_by=owner.id,
    ))
    db_session.flush()

    response = void(client, owner_headers, invoice)
    assert response.status_code == 409
    assert "payments" in response.json()["detail"]
    assert stock_of(client, owner_headers, shop["rice"]) == 8  # untouched


# --- listing, history, isolation ----------------------------------------------

def test_list_and_filter_invoices(client, owner_headers, shop):
    first = create_invoice(client, owner_headers, shop)
    create_invoice(client, owner_headers, shop)
    confirm(client, owner_headers, first)

    all_invoices = client.get(INVOICES_URL, headers=owner_headers).json()
    assert [i["invoice_number"] for i in all_invoices] == ["INV-00002", "INV-00001"]  # newest first

    confirmed = client.get(INVOICES_URL, params={"status": "confirmed"}, headers=owner_headers).json()
    assert [i["invoice_number"] for i in confirmed] == ["INV-00001"]

    assert client.get(INVOICES_URL, params={"status": "bogus"}, headers=owner_headers).status_code == 422


def test_customer_invoice_history(client, owner_headers, shop):
    create_invoice(client, owner_headers, shop)
    other_customer = client.post(
        "/api/v1/customers", json={"full_name": "Bola Ahmed"}, headers=owner_headers
    ).json()["id"]
    client.post(INVOICES_URL, json={"customer_id": other_customer}, headers=owner_headers)

    history = client.get(f"/api/v1/customers/{shop['customer']}/invoices", headers=owner_headers).json()
    assert [i["invoice_number"] for i in history] == ["INV-00001"]


def test_invoices_isolated_between_businesses(client, owner_headers, other_owner_headers, shop):
    invoice = create_invoice(client, owner_headers, shop)

    assert client.get(INVOICES_URL, headers=other_owner_headers).json() == []
    assert client.get(f"{INVOICES_URL}/{invoice['id']}", headers=other_owner_headers).status_code == 404
    assert confirm(client, other_owner_headers, invoice).status_code == 404
    assert void(client, other_owner_headers, invoice).status_code == 404

    # Can't invoice another business's customer or product either.
    rival_customer = client.post(
        "/api/v1/customers", json={"full_name": "Rival Customer"}, headers=other_owner_headers
    ).json()["id"]
    assert client.post(
        INVOICES_URL, json={"customer_id": shop["customer"]}, headers=other_owner_headers
    ).status_code == 404
    assert client.post(
        INVOICES_URL,
        json={"customer_id": rival_customer, "items": [{"product_id": shop["rice"], "quantity": 1}]},
        headers=other_owner_headers,
    ).status_code == 404
