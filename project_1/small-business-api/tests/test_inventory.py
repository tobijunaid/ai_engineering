INVENTORY_URL = "/api/v1/inventory"

RICE = {"name": "Bag of Rice (50kg)", "sku": "RICE-50", "selling_price": "45000.00"}


def create_product(client, headers, product=RICE):
    response = client.post("/api/v1/products", json=product, headers=headers)
    assert response.status_code == 201
    return response.json()["id"]


def move(client, headers, product_id, movement_type, quantity, reason=None):
    return client.post(
        f"{INVENTORY_URL}/{product_id}/movements",
        json={"movement_type": movement_type, "quantity": quantity, "reason": reason},
        headers=headers,
    )


def stock_of(client, headers, product_id):
    return client.get(f"{INVENTORY_URL}/{product_id}", headers=headers).json()["quantity"]


# --- Stock levels ---------------------------------------------------------

def test_new_product_starts_with_zero_stock(client, owner_headers):
    product_id = create_product(client, owner_headers)
    response = client.get(f"{INVENTORY_URL}/{product_id}", headers=owner_headers)

    assert response.status_code == 200
    assert response.json()["quantity"] == 0
    assert response.json()["sku"] == "RICE-50"


def test_list_stock_levels(client, owner_headers):
    product_id = create_product(client, owner_headers)
    move(client, owner_headers, product_id, "stock_in", 10)

    response = client.get(INVENTORY_URL, headers=owner_headers)
    assert response.status_code == 200
    assert [(s["sku"], s["quantity"]) for s in response.json()] == [("RICE-50", 10)]


# --- Movements ------------------------------------------------------------

def test_stock_in_increases_stock(client, owner_headers):
    product_id = create_product(client, owner_headers)
    response = move(client, owner_headers, product_id, "stock_in", 20, "Supplier delivery")

    assert response.status_code == 201
    assert response.json()["movement_type"] == "stock_in"
    assert response.json()["quantity"] == 20
    assert response.json()["quantity_after"] == 20
    assert stock_of(client, owner_headers, product_id) == 20


def test_damage_and_return_change_stock_correctly(client, staff_headers):
    product_id = create_product(client, staff_headers)
    move(client, staff_headers, product_id, "stock_in", 20)
    move(client, staff_headers, product_id, "damage", 3, "Torn bags")
    response = move(client, staff_headers, product_id, "return", 1, "Customer return")

    assert response.json()["quantity_after"] == 18
    assert stock_of(client, staff_headers, product_id) == 18


def test_cannot_remove_more_stock_than_available(client, owner_headers):
    product_id = create_product(client, owner_headers)
    move(client, owner_headers, product_id, "stock_in", 5)

    response = move(client, owner_headers, product_id, "damage", 6)

    assert response.status_code == 409
    assert "Insufficient stock" in response.json()["detail"]
    assert stock_of(client, owner_headers, product_id) == 5  # unchanged


def test_manual_sale_movement_not_allowed(client, owner_headers):
    # Sales must come from confirmed invoices, never recorded by hand.
    product_id = create_product(client, owner_headers)
    response = move(client, owner_headers, product_id, "sale", 1)
    assert response.status_code == 422


def test_zero_or_negative_quantity_rejected(client, owner_headers):
    product_id = create_product(client, owner_headers)
    assert move(client, owner_headers, product_id, "stock_in", 0).status_code == 422
    assert move(client, owner_headers, product_id, "stock_in", -5).status_code == 422


def test_movement_history_is_recorded(client, owner_headers, db_session):
    product_id = create_product(client, owner_headers)
    move(client, owner_headers, product_id, "stock_in", 10)
    move(client, owner_headers, product_id, "damage", 2)

    response = client.get(f"{INVENTORY_URL}/{product_id}/movements", headers=owner_headers)
    assert response.status_code == 200

    # Compared without relying on order: inside one test transaction, PostgreSQL's
    # now() gives every row the same created_at timestamp.
    history = {(m["movement_type"], m["quantity"], m["quantity_after"]) for m in response.json()}
    assert history == {("stock_in", 10, 10), ("damage", 2, 8)}


# --- Adjustments (stocktake) ----------------------------------------------

def test_owner_can_adjust_stock_down_and_up(client, owner_headers):
    product_id = create_product(client, owner_headers)
    move(client, owner_headers, product_id, "stock_in", 50)

    down = client.post(
        f"{INVENTORY_URL}/{product_id}/adjust",
        json={"new_quantity": 47, "reason": "Stocktake: 3 missing"},
        headers=owner_headers,
    )
    assert down.status_code == 201
    assert down.json()["quantity"] == 3
    assert down.json()["quantity_after"] == 47

    up = client.post(
        f"{INVENTORY_URL}/{product_id}/adjust",
        json={"new_quantity": 49, "reason": "Found 2 in back store"},
        headers=owner_headers,
    )
    assert up.json()["quantity"] == 2
    assert up.json()["quantity_after"] == 49


def test_adjust_to_same_quantity_rejected(client, owner_headers):
    product_id = create_product(client, owner_headers)
    response = client.post(
        f"{INVENTORY_URL}/{product_id}/adjust",
        json={"new_quantity": 0, "reason": "No change"},
        headers=owner_headers,
    )
    assert response.status_code == 400


def test_adjust_requires_reason(client, owner_headers):
    product_id = create_product(client, owner_headers)
    response = client.post(
        f"{INVENTORY_URL}/{product_id}/adjust",
        json={"new_quantity": 5},
        headers=owner_headers,
    )
    assert response.status_code == 422


def test_staff_cannot_adjust_stock(client, owner_headers, staff_headers):
    product_id = create_product(client, owner_headers)
    response = client.post(
        f"{INVENTORY_URL}/{product_id}/adjust",
        json={"new_quantity": 5, "reason": "test"},
        headers=staff_headers,
    )
    assert response.status_code == 403


# --- Business isolation ---------------------------------------------------

def test_cannot_touch_another_business_inventory(client, owner_headers, other_owner_headers):
    product_id = create_product(client, owner_headers)
    move(client, owner_headers, product_id, "stock_in", 10)

    assert client.get(INVENTORY_URL, headers=other_owner_headers).json() == []
    assert client.get(f"{INVENTORY_URL}/{product_id}", headers=other_owner_headers).status_code == 404
    assert move(client, other_owner_headers, product_id, "damage", 10).status_code == 404
    assert client.get(
        f"{INVENTORY_URL}/{product_id}/movements", headers=other_owner_headers
    ).status_code == 404

    assert stock_of(client, owner_headers, product_id) == 10  # untouched
