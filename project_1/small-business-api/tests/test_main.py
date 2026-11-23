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


def test_register_duplicate_email(client):
    # First registration
    response1 = client.post("/api/v1/auth/register", json={
        "business_name": "Tobi Stores",
        "full_name": "Tobi Junaid",
        "email": "tobi_test@example.com",
        "password": "TestPassword123"
    })

    # Attempt to register with the same email
    response2 = client.post("/api/v1/auth/register", json={
        "business_name": "Another Business",
        "full_name": "Another Name",
        "email": "tobi_test@example.com",
        "password": "AnotherPassword456"
    })

    assert response1.status_code == 201
    assert response2.status_code == 409
    assert response2.json()["detail"] == "Email is already registered."
    
def test_login_success(client):
    # First, register the user
    client.post("/api/v1/auth/register", json={
        "business_name": "Tobi Stores",
        "full_name": "Tobi Junaid",
        "email": "tobi_test@example.com",
        "password": "TestPassword123"
    })

    # Then, log in
    response = client.post("/api/v1/auth/login", data={
        "username": "tobi_test@example.com",
        "password": "TestPassword123"
    })

    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
    
def test_login_invalid_password(client):
    client.post("/api/v1/auth/register", json={
        "business_name": "Tobi Stores",
        "full_name": "Tobi Junaid",
        "email": "tobi_test@example.com",
        "password": "TestPassword123"
    })

    response = client.post("/api/v1/auth/login", data={
        "username": "tobi_test@example.com",
        "password": "WrongPassword456"
    })
    
    assert response.status_code == 401 
    assert response.json()["detail"] == "Invalid email or password."
    
def test_get_current_user(client):
    # Register and log in the user
    client.post("/api/v1/auth/register", json={
        "business_name": "Tobi Stores",
        "full_name": "Tobi Junaid",
        "email": "tobi_test@example.com",
        "password": "TestPassword123"
    })

    # Log in the user
    login_response = client.post("/api/v1/auth/login", data={
        "username": "tobi_test@example.com",
        "password": "TestPassword123"
    })
    
    access_token = login_response.json()["access_token"]

    # Get the current user
    response = client.get("/api/v1/auth/me",headers =
                        {"Authorization": f"Bearer {access_token}"})
    

    assert response.status_code == 200
    assert response.json()["email"] == "tobi_test@example.com"
    

def test_get_current_user_without_token(client):
    response = client.get("/api/v1/auth/me")

    assert response.status_code == 401
    

def test_staff_cannot_access_owner_endpoints(client):
    # Register owner
    response1 = client.post("/api/v1/auth/register", json={
            "business_name": "Tobi Stores",
            "full_name": "Tobi Junaid",
            "email": "tobi_test@example.com",
            "password": "TestPassword123"
        })

    # Log in the owner
    login_response1 = client.post("/api/v1/auth/login", data={
        "username": "tobi_test@example.com",
        "password": "TestPassword123"
    })
    
    owner_token = login_response1.json()["access_token"]
    
    #Register Staff
    response = client.post("/api/v1/auth/staff", json={
        "full_name": "David Smith",
        "email": "david_test@example.com",
        "password": "StaffPassword123"
    },
    headers={"Authorization": f"Bearer {owner_token}"}
)
    
    login_response2 = client.post("/api/v1/auth/login", data={
            "username": "david_test@example.com",
            "password": "StaffPassword123"
        })

    access_token = login_response2.json()["access_token"]

    # Attempt to access owner-only endpoint
    response2 = client.get("/api/v1/auth/owner-check", headers={
        "Authorization": f"Bearer {access_token}"
    })

    assert response.status_code == 201
    assert response2.status_code == 403
    

def test_owner_can_access_owner_endpoint(client):
    # Register owner
    response1 = client.post("/api/v1/auth/register", json={
        "business_name": "Tobi Stores",
        "full_name": "Tobi Junaid",
        "email": "tobi_test@example.com",
        "password": "TestPassword123"
    })

    assert response1.status_code == 201

    # Log in the owner
    login_response1 = client.post("/api/v1/auth/login", data={
        "username": "tobi_test@example.com",
        "password": "TestPassword123"
    })

    access_token = login_response1.json()["access_token"]

    # Access owner-only endpoint
    response2 = client.get(
        "/api/v1/auth/owner-check",
        headers={"Authorization": f"Bearer {access_token}"}
    )

    assert response2.status_code == 200
    
def test_deactivated_staff_cannot_access_protected_route(client):
        # Register owner
        response1 = client.post("/api/v1/auth/register", json={
                "business_name": "Tobi Stores",
                "full_name": "Tobi Junaid",
                "email": "tobi_test@example.com",
                "password": "TestPassword123"
            })
    
        # Log in the owner
        login_response1 = client.post("/api/v1/auth/login", data={
            "username": "tobi_test@example.com",
            "password": "TestPassword123"
        })
        
        owner_token = login_response1.json()["access_token"]
        
        #Register Staff
        response2 = client.post("/api/v1/auth/staff", json={
            "full_name": "David Smith",
            "email": "david_test@example.com",
            "password": "StaffPassword123"
        },
        headers={"Authorization": f"Bearer {owner_token}"}
    )
        
        login_response2 = client.post("/api/v1/auth/login", data={
                "username": "david_test@example.com",
                "password": "StaffPassword123"
            })
    
        access_token = login_response2.json()["access_token"]
        
        staff_id = response2.json()["id"]

        response3 = client.patch(
        f"/api/v1/auth/staff/{staff_id}/deactivate",
        headers={"Authorization": f"Bearer {owner_token}"}
    )
        
        response4 = client.get("/api/v1/auth/me",headers =
                                {"Authorization": f"Bearer {access_token}"})
        
        assert response4.status_code == 401
        assert response3.status_code == 200
        
def test_reactivated_staff_can_access_protected_route(client):
            # Register owner
            response1 = client.post("/api/v1/auth/register", json={
                    "business_name": "Tobi Stores",
                    "full_name": "Tobi Junaid",
                    "email": "tobi_test@example.com",
                    "password": "TestPassword123"
                })
        
            # Log in the owner
            login_response1 = client.post("/api/v1/auth/login", data={
                "username": "tobi_test@example.com",
                "password": "TestPassword123"
                })
            
            owner_token = login_response1.json()["access_token"]
            
            #Register Staff
            response2 = client.post("/api/v1/auth/staff", json={
                "full_name": "David Smith",
                "email": "david_test@example.com",
                "password": "StaffPassword123"
                },
            headers={"Authorization": f"Bearer {owner_token}"
                })
            
            login_response2 = client.post("/api/v1/auth/login", data={
                    "username": "david_test@example.com",
                    "password": "StaffPassword123"
                })
        
            access_token = login_response2.json()["access_token"]
            
            staff_id = response2.json()["id"]
    
            response3 = client.patch(
                f"/api/v1/auth/staff/{staff_id}/deactivate",
                headers={"Authorization": f"Bearer {owner_token}"
                })
            
            response4 = client.get("/api/v1/auth/me",headers =
                                    {"Authorization": f"Bearer {access_token}"})
            
            #Reactivate Staff
            response5 = client.patch(
                f"/api/v1/auth/staff/{staff_id}/reactivate",
                headers={"Authorization": f"Bearer {owner_token}"
                })
            
            # Get the current user
            response6 = client.get("/api/v1/auth/me",headers =
                        {"Authorization": f"Bearer {access_token}"})
            
            assert response1.status_code == 201
            assert login_response1.status_code == 200
            assert response2.status_code == 201
            assert login_response2.status_code == 200
            assert response4.status_code == 401
            assert response3.status_code == 200
            assert response5.status_code == 200
            assert response6.json()["email"] == "david_test@example.com"
            assert response6.json()["role"] == "staff"

def test_owner_cannot_access_another_business_staff(client):
                # Register Tobi Stores owner
                response1 = client.post("/api/v1/auth/register", json={
                        "business_name": "Tobi Stores",
                        "full_name": "Tobi Junaid",
                        "email": "tobi_test@example.com",
                        "password": "TestPassword123"
                    })
            
                # Log in Tobi Stores
                login_response1 = client.post("/api/v1/auth/login", data={
                    "username": "tobi_test@example.com",
                    "password": "TestPassword123"
                    })
                
                owner_token = login_response1.json()["access_token"]
                
                #Register Staff
                response2 = client.post("/api/v1/auth/staff", json={
                    "full_name": "David Smith",
                    "email": "david_test@example.com",
                    "password": "StaffPassword123",
                    "is_active": True
                    },
                headers={"Authorization": f"Bearer {owner_token}"
                    })
                
                david_id = response2.json()["id"]
                
                # Register Grace Stores owner
                response3 = client.post("/api/v1/auth/register", json={
                        "business_name": "Grace Stores",
                        "full_name": "Grace Junaid",
                        "email": "grace_test@example.com",
                        "password": "Test2Password123"
                    })
            
                # Log in Grace Stores
                login_response2 = client.post("/api/v1/auth/login", data={
                    "username": "grace_test@example.com",
                    "password": "Test2Password123"
                    })
                
                owner_token2 = login_response2.json()["access_token"]
                
                #Register Grace Staff
                response4 = client.post("/api/v1/auth/staff", json={
                    "full_name": "Sarah Smith",
                    "email": "sarah_test@example.com",
                    "password": "Staff2Password123",
                    "is_active": True
                    },
                headers={"Authorization": f"Bearer {owner_token2}"
                    })
                
                sarah_id = response4.json()["id"]
                
                response5 = client.patch(
                    f"/api/v1/auth/staff/{sarah_id}/deactivate",
                    headers={"Authorization": f"Bearer {owner_token}"}
                )
                response6 = client.patch(
                    f"/api/v1/auth/staff/{sarah_id}/reactivate",
                    headers={"Authorization": f"Bearer {owner_token}"}
                )
                
                response8 = client.get("/api/v1/auth/staff",
                    headers={"Authorization": f"Bearer {owner_token2}"}
                )

                staff_list = response8.json()
                sarah = next(
                    staff for staff in staff_list
                    if staff["id"] == str(sarah_id)
                )

                
                assert response1.status_code == 201
                assert response2.status_code == 201
                assert response3.status_code == 201
                assert response4.status_code == 201
                assert response6.status_code == 404
                assert response5.status_code == 404
                assert response8.status_code == 200
                assert len(staff_list) == 1
                assert sarah["is_active"] is True