import pytest
from pydantic import ValidationError
from hello_python.models.user import User, Role

def test_user_ok_normalizes_email():
    u = User(id=1, email="  Test@Example.COM  ", role="admin")
    assert u.id == 1
    assert u.email == "test@example.com"
    assert u.role is Role.admin

@pytest.mark.parametrize("bad_email", [
    "", "   ", "foo", "a@b", "a@b.", "a@.com", "@example.com", "user@",
])
def test_user_bad_email(bad_email: str):
    with pytest.raises(ValidationError):
        User(id=1, email=bad_email, role="user")

@pytest.mark.parametrize("bad_id", [0, -1])
def test_user_bad_id(bad_id: int):
    with pytest.raises(ValidationError):
        User(id=bad_id, email="ok@example.com", role="user")

def test_user_bad_role():
    with pytest.raises(ValidationError):
        User(id=1, email="ok@example.com", role="owner")  # no está en Enum
