from __future__ import annotations

from enum import Enum
from pydantic import BaseModel, Field, field_validator, EmailStr

EMAIL_RE = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    moderator = "moderator"

class User(BaseModel):
    id: int = Field(ge=1)
    # email: EmailStr
    email: str = Field(pattern=EMAIL_RE)
    role: Role

    @field_validator("email", mode="before")
    @classmethod
    def normalize_email(cls, v: str) -> str:
        v = v.strip().lower()
        if not v:
            raise ValueError("emaul must not be empty")
        return v