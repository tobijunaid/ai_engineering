CUSTOMERS_URL = "/api/v1/customers"

ADA = {
    "full_name": "Adaeze Okafor",
    "email": "ada@example.com",
    "phone": "+2348012345678",
    "address": "12 Allen Avenue, Ikeja",
}


def create_customer(client, headers, data=ADA):
    response = client.post(CUSTOMERS_URL, json=data, headers=headers)
    assert response.status_code == 201
    return response.json()


def test_create_customer(client, owner_headers):
    customer = create_customer(client, owner_headers)
    assert customer["full_name"] == "Adaeze Okafor"
    assert customer["email"] == "ada@example.com"


def test_create_customer_with_name_only(client, staff_headers):
    customer = create_customer(client, staff_headers, {"full_name": "Walk-in Customer"})
    assert customer["email"] is None
    assert customer["phone"] is None


def test_invalid_email_rejected(client, owner_headers):
    response = client.post(
        CUSTOMERS_URL, json={**ADA, "email": "not-an-email"}, headers=owner_headers
    )
    assert response.status_code == 422


def test_create_customer_requires_auth(client):
    assert client.post(CUSTOMERS_URL, json=ADA).status_code == 401


def test_list_and_get_customer(client, owner_headers):
    customer = create_customer(client, owner_headers)

    listed = client.get(CUSTOMERS_URL, headers=owner_headers).json()
    assert [c["id"] for c in listed] == [customer["id"]]

    response = client.get(f"{CUSTOMERS_URL}/{customer['id']}", headers=owner_headers)
    assert response.status_code == 200
    assert response.json()["phone"] == ADA["phone"]


def test_search_customers(client, owner_headers):
    create_customer(client, owner_headers)
    create_customer(client, owner_headers, {"full_name": "Bola Ahmed", "phone": "+2347099999999"})

    def names(search):
        response = client.get(CUSTOMERS_URL, params={"search": search}, headers=owner_headers)
        return [c["full_name"] for c in response.json()]

    assert names("ada") == ["Adaeze Okafor"]        # name, case-insensitive
    assert names("example.com") == ["Adaeze Okafor"]  # email
    assert names("70999") == ["Bola Ahmed"]          # phone
    assert names("zzz") == []


def test_update_customer(client, owner_headers):
    customer = create_customer(client, owner_headers)
    response = client.patch(
        f"{CUSTOMERS_URL}/{customer['id']}",
        json={"phone": "+2348000000000", "email": None},  # change phone, clear email
        headers=owner_headers,
    )
    assert response.status_code == 200
    assert response.json()["phone"] == "+2348000000000"
    assert response.json()["email"] is None
    assert response.json()["full_name"] == ADA["full_name"]  # untouched


def test_update_full_name_to_null_rejected(client, owner_headers):
    customer = create_customer(client, owner_headers)
    response = client.patch(
        f"{CUSTOMERS_URL}/{customer['id']}", json={"full_name": None}, headers=owner_headers
    )
    assert response.status_code == 422


def test_customers_isolated_between_businesses(client, owner_headers, other_owner_headers):
    customer = create_customer(client, owner_headers)
    url = f"{CUSTOMERS_URL}/{customer['id']}"

    assert client.get(CUSTOMERS_URL, headers=other_owner_headers).json() == []
    assert client.get(url, headers=other_owner_headers).status_code == 404
    assert client.patch(url, json={"full_name": "Hijacked"}, headers=other_owner_headers).status_code == 404
