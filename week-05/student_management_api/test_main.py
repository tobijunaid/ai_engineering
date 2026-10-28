# TestClient(app) lets Python send requests to your FastAPI application without starting Uvicorn.
# client.post(...) simulates a client creating a student.
# json=... supplies the request body.
# assert checks whether the actual result matches what you expect. If an assertion fails, pytest reports a failed test.

import pytest
from fastapi.testclient import TestClient
from main import app
from main import app, students

client = TestClient(app)


def test_create_student():
    response = client.post(
        "/students",
        json={"name": "Test Student", "age": 20}
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Test Student"
    assert response.json()["age"] == 20


def test_duplicate_student():
    client.post(
        "/students",
        json={"name": "Duplicate Student", "age": 20}
    )

    response = client.post(
        "/students",
        json={"name": "Duplicate Student", "age": 22}
    )

    assert response.status_code == 409
    assert "already exists" in response.json()["detail"]


def test_student_not_found():
    response = client.get("/students/UnknownStudent")

    assert response.status_code == 404
    assert response.json()["detail"] == "Student 'UnknownStudent' not found"


@pytest.fixture(autouse=True)
def clear_students():
    students.clear()
    

def test_create_student_with_invalid_name():
    response = client.post(
        "/students",
        json={"name": "T", "age": 20}
    )

    assert response.status_code == 422


def test_create_student_with_invalid_age():
    response = client.post(
        "/students",
        json={"name": "Test Student", "age": 0}
    )

    assert response.status_code == 422


def test_update_student():
    client.post(
        "/students",
        json={"name": "Update Test", "age": 20}
    )

    response = client.put(
        "/students/Update Test",
        json={"age": 25}
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Update Test"
    assert response.json()["age"] == 25

def test_delete_student():
    client.post(
        "/students",
        json={"name": "Delete Test", "age": 21}
    )

    response = client.delete("/students/Delete Test")

    assert response.status_code == 200
    assert response.json()["name"] == "Delete Test"
    assert response.json()["message"] == "Student deleted successfully"

    # Confirm the student was actually removed
    get_response = client.get("/students/Delete Test")
    assert get_response.status_code == 404


def test_get_all_students():
    client.post(
        "/students",
        json={"name": "Tobi", "age": 23}
    )

    client.post(
        "/students",
        json={"name": "David", "age": 24}
    )

    response = client.get("/students")

    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["name"] == "Tobi"
    assert response.json()[1]["name"] == "David"


def test_update_student_not_found():
    response = client.put(
        "/students/UnknownStudent",
        json={"age": 25}
    )

    assert response.status_code == 404
    assert response.json()["detail"] == (
        "Student 'UnknownStudent' not found"
    )

def test_delete_student_not_found():
    response = client.delete("/students/UnknownStudent")

    assert response.status_code == 404
    assert response.json()["detail"] == (
        "Student 'UnknownStudent' not found"
    )
