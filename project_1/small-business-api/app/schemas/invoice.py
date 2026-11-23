from datetime import datetime
from decimal import Decimal
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, Field


class InvoiceItemCreate(BaseModel):
    product_id: UUID
    quantity: int = Field(gt=0)


class InvoiceItemUpdate(BaseModel):
    quantity: int = Field(gt=0)


class InvoiceCreate(BaseModel):
    customer_id: UUID
    # Items are optional: a draft can be created empty and filled in later.
    items: list[InvoiceItemCreate] = []


class InvoiceVoid(BaseModel):
    reason: str = Field(min_length=1, max_length=500)  # required for the audit trail


InvoiceStatus = Literal["draft", "confirmed", "void"]


class InvoiceItemResponse(BaseModel):
    id: UUID
    product_id: UUID
    product_name: str     # snapshot: stays the same even if the product is renamed later
    quantity: int
    unit_price: Decimal   # snapshot of the price at the time it was added
    line_total: Decimal

    model_config = {"from_attributes": True}


class InvoiceResponse(BaseModel):
    id: UUID
    invoice_number: str
    customer_id: UUID
    status: str
    payment_status: str
    subtotal: Decimal
    total: Decimal
    items: list[InvoiceItemResponse]
    created_by: UUID
    confirmed_at: datetime | None
    voided_at: datetime | None
    voided_by: UUID | None
    void_reason: str | None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
