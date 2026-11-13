'''What is conftest.py?
Pytest automatically discovers this special file and makes fixtures defined inside it available to test files throughout the relevant test directory.
Instead of defining the same test client in every test file, we define it once.'''

import pytest
from fastapi.testclient import TestClient #TestClient: Allows us to simulate HTTP requests to FastAPI.

from app.main import app #app: Imports your actual FastAPI application.


@pytest.fixture #@pytest.fixture: Makes client reusable.
def client():
    return TestClient(app) #TestClient(app): Creates a test client connected to your application.