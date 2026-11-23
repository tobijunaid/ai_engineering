from datetime import datetime
from decimal import Decimal
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, Field

# The DB column is a free-text String(30); the API restricts it to known methods.
PaymentMethod = Literal["cash", "bank_transfer", "card", "mobile_money", "other"]


class PaymentCreate(BaseModel):
    amount: Decimal = Field(gt=0, max_digits=12, decimal_places=2)
    payment_method: PaymentMethod
    # e.g. a bank transfer reference or POS receipt number
    reference: str | None = Field(default=None, max_length=100)


class PaymentResponse(BaseModel):
    id: UUID
    invoice_id: UUID
    amount: Decimal
    payment_method: str
    reference: str | None
    recorded_by: UUID
    created_at: datetime

    model_config = {"from_attributes": True}
