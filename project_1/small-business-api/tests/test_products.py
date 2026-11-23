from sqlalchemy import select

from app.models import Inventory

PRODUCTS_URL = "/api/v1/products"

RICE = {
    "name": "Bag of Rice (50kg)",
    "description": "Long grain parboiled rice",
    "sku": "RICE-50",
    "selling_price": "45000.00",
}


def create_rice(client, headers):
    response = client.post(PRODUCTS_URL, json=RICE, headers=headers)
    assert response.status_code == 201
    return response.json()


# --- Create ---------------------------------------------------------------

def test_create_product(client, owner_headers, db_session):
    product = create_rice(client, owner_headers)

    assert product["name"] == RICE["name"]
    assert product["sku"] == "RICE-50"
    assert product["selling_price"] == "45000.00"
    assert product["is_active"] is True

    # Creating a product must also create its inventory row, starting at 0.
    inventory = db_session.scalar(
        select(Inventory).where(Inventory.product_id == product["id"])
    )
    assert inventory is not None
    assert inventory.quantity == 0


def test_staff_can_create_product(client, staff_headers):
    response = client.post(PRODUCTS_URL, json=RICE, headers=staff_headers)
    assert response.status_code == 201


def test_create_product_requires_auth(client):
    response = client.post(PRODUCTS_URL, json=RICE)
    assert response.status_code == 401


def test_duplicate_sku_in_same_business_rejected(client, owner_headers):
    create_rice(client, owner_headers)
    response = client.post(PRODUCTS_URL, json=RICE, headers=owner_headers)

    assert response.status_code == 409


def test_same_sku_allowed_in_different_businesses(client, owner_headers, other_owner_headers):
    create_rice(client, owner_headers)
    response = client.post(PRODUCTS_URL, json=RICE, headers=other_owner_headers)

    assert response.status_code == 201


def test_negative_price_rejected(client, owner_headers):
    response = client.post(
        PRODUCTS_URL, json={**RICE, "selling_price": "-1"}, headers=owner_headers
    )
    assert response.status_code == 422


# --- Read -----------------------------------------------------------------

def test_list_products(client, owner_headers):
    create_rice(client, owner_headers)
    response = client.get(PRODUCTS_URL, headers=owner_headers)

    assert response.status_code == 200
    assert [p["sku"] for p in response.json()] == ["RICE-50"]


def test_get_single_product(client, owner_headers):
    product = create_rice(client, owner_headers)
    response = client.get(f"{PRODUCTS_URL}/{product['id']}", headers=owner_headers)

    assert response.status_code == 200
    assert response.json()["id"] == product["id"]


def test_cannot_see_another_business_products(client, owner_headers, other_owner_headers):
    product = create_rice(client, owner_headers)

    # Not in the rival's list...
    response = client.get(PRODUCTS_URL, headers=other_owner_headers)
    assert response.json() == []

    # ...and fetching it directly looks like it doesn't exist.
    response = client.get(f"{PRODUCTS_URL}/{product['id']}", headers=other_owner_headers)
    assert response.status_code == 404


# --- Update ---------------------------------------------------------------

def test_partial_update_product(client, owner_headers):
    product = create_rice(client, owner_headers)
    response = client.patch(
        f"{PRODUCTS_URL}/{product['id']}",
        json={"selling_price": "47500.50"},
        headers=owner_headers,
    )

    assert response.status_code == 200
    assert response.json()["selling_price"] == "47500.50"
    assert response.json()["name"] == RICE["name"]  # untouched fields unchanged


def test_update_to_existing_sku_rejected(client, owner_headers):
    create_rice(client, owner_headers)
    beans = client.post(
        PRODUCTS_URL, json={**RICE, "name": "Beans", "sku": "BEANS-1"}, headers=owner_headers
    ).json()

    response = client.patch(
        f"{PRODUCTS_URL}/{beans['id']}", json={"sku": "RICE-50"}, headers=owner_headers
    )
    assert response.status_code == 409


def test_cannot_update_another_business_product(client, owner_headers, other_owner_headers):
    product = create_rice(client, owner_headers)
    response = client.patch(
        f"{PRODUCTS_URL}/{product['id']}", json={"name": "Hacked"}, headers=other_owner_headers
    )
    assert response.status_code == 404


# --- Deactivate / reactivate ---------------------------------------------

def test_owner_can_deactivate_and_reactivate(client, owner_headers):
    product = create_rice(client, owner_headers)

    response = client.patch(f"{PRODUCTS_URL}/{product['id']}/deactivate", headers=owner_headers)
    assert response.status_code == 200
    assert response.json()["is_active"] is False

    # Hidden from the default list, visible with include_inactive=true.
    assert client.get(PRODUCTS_URL, headers=owner_headers).json() == []
    all_products = client.get(
        PRODUCTS_URL, params={"include_inactive": True}, headers=owner_headers
    ).json()
    assert len(all_products) == 1

    response = client.patch(f"{PRODUCTS_URL}/{product['id']}/reactivate", headers=owner_headers)
    assert response.json()["is_active"] is True


def test_staff_cannot_deactivate_product(client, owner_headers, staff_headers):
    product = create_rice(client, owner_headers)
    response = client.patch(f"{PRODUCTS_URL}/{product['id']}/deactivate", headers=staff_headers)

    assert response.status_code == 403
