from datetime import datetime
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, Field


# Manual movements a user may record directly.
# "sale" is deliberately excluded: sales only happen when an invoice is confirmed.
# "adjustment" has its own endpoint because it takes a counted total, not a change.
ManualMovementType = Literal["stock_in", "return", "damage"]


class MovementCreate(BaseModel):
    movement_type: ManualMovementType
    quantity: int = Field(gt=0)
    reason: str | None = Field(default=None, max_length=500)


class StockAdjustment(BaseModel):
    # The quantity physically counted on the shelf (e.g. during a stocktake).
    new_quantity: int = Field(ge=0)
    reason: str = Field(min_length=1, max_length=500)  # required: adjustments must be explained


class StockLevelResponse(BaseModel):
    product_id: UUID
    product_name: str
    sku: str
    quantity: int
    updated_at: datetime


class MovementResponse(BaseModel):
    id: UUID
    product_id: UUID
    movement_type: str
    quantity: int
    quantity_after: int
    reason: str | None
    reference_id: UUID | None
    created_by: UUID
    created_at: datetime

    model_config = {"from_attributes": True}
