from urllib import response
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import Business, User


def test_root_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to the Small Business Inventory API"
    

def test_register_business(client, db_session):
    response = client.post("/api/v1/auth/register", json={
    "business_name": "Tobi Stores",
    "full_name": "Tobi Junaid",
    "email": "tobi_test@example.com",
    "password": "TestPassword123"
})

    assert response.status_code == 201
    assert response.json()["email"] == "tobi_test@example.com"
    assert response.json()["role"] == "owner"

business = db_session.scalar(
    select(Business).where(Business.name == "Tobi Stores")
)

user = db_session.scalar(
    select(User).where(User.email == "tobi_test@example.com")
)

assert business is not None
assert user is not None
assert user.business_id == business.id
