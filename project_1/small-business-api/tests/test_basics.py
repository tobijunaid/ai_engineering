def test_addition():
    result = 10 + 5
    
    assert result == 15
    
import pytest

'''
There are three important benefits of pytest.fixture:
1. Reusability: Multiple tests can use the same fixture.
2. Consistency: Tests receive the same predictable starting data.
3. Maintainability: If the sample data changes, you update it in one place.
'''

@pytest.fixture
def sample_user():
    return {
        "full_name": "David Smith",
        "email": "david@example.com",
        "role": "staff",
    }


def test_user_email(sample_user):
    assert sample_user["email"] == "david@example.com"


def test_user_role(sample_user):
    assert sample_user["role"] == "staff"