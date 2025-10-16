import pytest


@pytest.fixture
def sample_user():
    return {"name": "Abraham", "age": 34}


def test_user_name(sample_user):
    assert sample_user["name"] == "Abraham"
