from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, Field


# ProductCreate: what a client must send to create a product.
# Stock quantity is deliberately NOT here — stock changes belong to the inventory
# module so that every change produces an inventory movement record (design rule 6.1).
class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=150)
    description: str | None = None
    sku: str = Field(min_length=1, max_length=50)
    # Decimal (not float) because money must be exact: 0.1 + 0.2 != 0.3 in floats.
    selling_price: Decimal = Field(ge=0, max_digits=12, decimal_places=2)


# ProductUpdate: every field optional, so a PATCH can change just one thing.
class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=150)
    description: str | None = None
    sku: str | None = Field(default=None, min_length=1, max_length=50)
    selling_price: Decimal | None = Field(
        default=None, ge=0, max_digits=12, decimal_places=2
    )


class ProductResponse(BaseModel):
    id: UUID
    business_id: UUID
    name: str
    description: str | None
    sku: str
    selling_price: Decimal
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
