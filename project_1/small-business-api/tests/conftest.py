'''What is conftest.py?
Pytest automatically discovers this special file and makes fixtures defined inside it available to test files throughout the relevant test directory.
Instead of defining the same test client in every test file, we define it once.'''

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.engine import make_url
from sqlalchemy.orm import Session

import app.models
from app.core.config import settings
from app.db.dependencies import get_db
from app.db.session import Base
from app.main import app


# @pytest.fixture #@pytest.fixture: Makes client reusable.
# def client():
#     return TestClient(app) #TestClient(app): Creates a test client connected to your application.

@pytest.fixture(scope="session")
def test_engine(): #test_engine: connects only to small_business_test_db, creates the tables before testing, and drops them after the test session.
    database_url = settings.test_database_url

    if not database_url:
        raise RuntimeError("TEST_DATABASE_URL is not configured.")

    # Safety check: never allow tests to use the development database.
    database_name = make_url(database_url).database

    if database_name != "small_business_test_db":
        raise RuntimeError(
            f"Refusing to run tests against unexpected database: {database_name}"
        )

    engine = create_engine(database_url)

    Base.metadata.create_all(bind=engine)

    yield engine

    Base.metadata.drop_all(bind=engine)
    engine.dispose()


@pytest.fixture
def db_session(test_engine): #db_session: gives each test its own database transaction and rolls it back afterward, even if application code calls commit()
    connection = test_engine.connect()
    transaction = connection.begin()

    session = Session(
        bind=connection,
        join_transaction_mode="create_savepoint",
    )

    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()


@pytest.fixture
def client(db_session): #client: overrides FastAPI's normal database dependency so API requests use the test session.
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.clear()