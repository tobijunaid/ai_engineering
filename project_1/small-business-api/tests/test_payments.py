import pytest

INVOICES_URL = "/api/v1/invoices"


def payments_url(invoice_id):
    return f"{INVOICES_URL}/{invoice_id}/payments"


def pay(client, headers, invoice_id, amount, method="cash", reference=None):
    return client.post(
        payments_url(invoice_id),
        json={"amount": amount, "payment_method": method, "reference": reference},
        headers=headers,
    )


def get_invoice(client, headers, invoice_id):
    return client.get(f"{INVOICES_URL}/{invoice_id}", headers=headers).json()


@pytest.fixture
def draft_invoice_id(client, owner_headers):
    """A draft invoice for 2 x 45,000.00 = 90,000.00."""
    customer_id = client.post(
        "/api/v1/customers", json={"full_name": "Adaeze Okafor"}, headers=owner_headers
    ).json()["id"]
    product_id = client.post(
        "/api/v1/products",
        json={"name": "Rice 50kg", "sku": "RICE-50", "selling_price": "45000.00"},
        headers=owner_headers,
    ).json()["id"]
    client.post(
        f"/api/v1/inventory/{product_id}/movements",
        json={"movement_type": "stock_in", "quantity": 10},
        headers=owner_headers,
    )
    return client.post(
        INVOICES_URL,
        json={"customer_id": customer_id, "items": [{"product_id": product_id, "quantity": 2}]},
        headers=owner_headers,
    ).json()["id"]


@pytest.fixture
def invoice_id(client, owner_headers, draft_invoice_id):
    """The same invoice, confirmed (so it can be paid)."""
    client.post(f"{INVOICES_URL}/{draft_invoice_id}/confirm", headers=owner_headers)
    return draft_invoice_id


# --- recording payments ---------------------------------------------------------

def test_new_confirmed_invoice_is_unpaid(client, owner_headers, invoice_id):
    invoice = get_invoice(client, owner_headers, invoice_id)
    assert invoice["payment_status"] == "unpaid"
    assert invoice["amount_paid"] == "0.00"
    assert invoice["balance_due"] == "90000.00"


def test_full_payment_marks_invoice_paid(client, owner_headers, invoice_id):
    response = pay(client, owner_headers, invoice_id, "90000.00", "bank_transfer", "TRF-12345")

    assert response.status_code == 201
    assert response.json()["amount"] == "90000.00"
    assert response.json()["reference"] == "TRF-12345"

    invoice = get_invoice(client, owner_headers, invoice_id)
    assert invoice["payment_status"] == "paid"
    assert invoice["balance_due"] == "0.00"


def test_partial_payments_until_paid(client, staff_headers, owner_headers, invoice_id):
    pay(client, staff_headers, invoice_id, "30000.00")
    invoice = get_invoice(client, owner_headers, invoice_id)
    assert invoice["payment_status"] == "partially_paid"
    assert invoice["amount_paid"] == "30000.00"
    assert invoice["balance_due"] == "60000.00"

    pay(client, staff_headers, invoice_id, "59999.99", "mobile_money")
    assert get_invoice(client, owner_headers, invoice_id)["payment_status"] == "partially_paid"

    pay(client, staff_headers, invoice_id, "0.01")  # the last kobo
    invoice = get_invoice(client, owner_headers, invoice_id)
    assert invoice["payment_status"] == "paid"
    assert invoice["balance_due"] == "0.00"


def test_overpayment_rejected(client, owner_headers, invoice_id):
    pay(client, owner_headers, invoice_id, "50000.00")
    response = pay(client, owner_headers, invoice_id, "40000.01")  # balance is 40,000.00

    assert response.status_code == 409
    assert "exceeds the outstanding balance" in response.json()["detail"]
    assert get_invoice(client, owner_headers, invoice_id)["amount_paid"] == "50000.00"


def test_cannot_pay_fully_paid_invoice(client, owner_headers, invoice_id):
    pay(client, owner_headers, invoice_id, "90000.00")
    assert pay(client, owner_headers, invoice_id, "1.00").status_code == 409


def test_cannot_pay_draft_invoice(client, owner_headers, draft_invoice_id):
    response = pay(client, owner_headers, draft_invoice_id, "1000.00")
    assert response.status_code == 409
    assert "confirmed" in response.json()["detail"]


def test_cannot_pay_void_invoice(client, owner_headers, invoice_id):
    client.post(f"{INVOICES_URL}/{invoice_id}/void", json={"reason": "Cancelled"}, headers=owner_headers)
    assert pay(client, owner_headers, invoice_id, "1000.00").status_code == 409


@pytest.mark.parametrize("amount", ["0", "-100.00", "10.001"])
def test_invalid_amounts_rejected(client, owner_headers, invoice_id, amount):
    assert pay(client, owner_headers, invoice_id, amount).status_code == 422


def test_unknown_payment_method_rejected(client, owner_headers, invoice_id):
    assert pay(client, owner_headers, invoice_id, "100.00", method="cheque").status_code == 422


def test_paid_invoice_cannot_be_voided(client, owner_headers, invoice_id):
    pay(client, owner_headers, invoice_id, "100.00")
    response = client.post(
        f"{INVOICES_URL}/{invoice_id}/void", json={"reason": "Changed mind"}, headers=owner_headers
    )
    assert response.status_code == 409


# --- listing & isolation ------------------------------------------------------

def test_list_payments(client, owner_headers, invoice_id):
    pay(client, owner_headers, invoice_id, "10000.00", "cash")
    pay(client, owner_headers, invoice_id, "20000.00", "card")

    response = client.get(payments_url(invoice_id), headers=owner_headers)
    assert response.status_code == 200
    assert sorted(p["amount"] for p in response.json()) == ["10000.00", "20000.00"]


def test_invoice_list_includes_balances(client, owner_headers, invoice_id):
    pay(client, owner_headers, invoice_id, "10000.00")
    invoices = client.get(INVOICES_URL, headers=owner_headers).json()
    assert invoices[0]["amount_paid"] == "10000.00"
    assert invoices[0]["balance_due"] == "80000.00"


def test_payments_isolated_between_businesses(client, owner_headers, other_owner_headers, invoice_id):
    pay(client, owner_headers, invoice_id, "10000.00")

    assert pay(client, other_owner_headers, invoice_id, "100.00").status_code == 404
    assert client.get(payments_url(invoice_id), headers=other_owner_headers).status_code == 404
