from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, field_validator


class CustomerCreate(BaseModel):
    full_name: str = Field(min_length=1, max_length=150)
    email: EmailStr | None = None
    phone: str | None = Field(default=None, max_length=30)
    address: str | None = None


class CustomerUpdate(BaseModel):
    full_name: str | None = Field(default=None, min_length=1, max_length=150)
    # email/phone/address CAN be cleared by sending null — those columns are nullable.
    email: EmailStr | None = None
    phone: str | None = Field(default=None, max_length=30)
    address: str | None = None

    @field_validator("full_name")
    @classmethod
    def reject_null(cls, value):
        if value is None:
            raise ValueError("cannot be null")
        return value


class CustomerResponse(BaseModel):
    id: UUID
    full_name: str
    email: str | None
    phone: str | None
    address: str | None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
