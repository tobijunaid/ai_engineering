from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import get_current_user, require_role
from app.db.dependencies import get_db
from app.models.user import User
from app.schemas.inventory import (
    MovementCreate,
    MovementResponse,
    StockAdjustment,
    StockLevelResponse,
)
from app.services.inventory_service import (
    InsufficientStockError,
    NoStockChangeError,
    adjust_stock,
    get_stock_level,
    list_movements,
    list_stock_levels,
    record_movement,
)
from app.services.product_service import ProductNotFoundError

router = APIRouter(prefix="/inventory", tags=["Inventory"])

'''
Permissions:
- Owners and staff can view stock and record stock_in / return / damage.
- Only owners can adjust stock to a counted total (it rewrites the books).
'''


def _not_found(error: Exception) -> HTTPException:
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))


@router.get("", response_model=list[StockLevelResponse])
def list_stock_endpoint(
    include_inactive: bool = False,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return list_stock_levels(db, current_user, include_inactive)


@router.get("/{product_id}", response_model=StockLevelResponse)
def get_stock_endpoint(
    product_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        return get_stock_level(db, current_user, product_id)
    except ProductNotFoundError as error:
        raise _not_found(error) from error


@router.post(
    "/{product_id}/movements",
    response_model=MovementResponse,
    status_code=status.HTTP_201_CREATED,
)
def record_movement_endpoint(
    product_id: UUID,
    data: MovementCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        return record_movement(db, current_user, product_id, data)
    except ProductNotFoundError as error:
        raise _not_found(error) from error
    except InsufficientStockError as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(error)) from error


@router.get("/{product_id}/movements", response_model=list[MovementResponse])
def list_movements_endpoint(
    product_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        return list_movements(db, current_user, product_id)
    except ProductNotFoundError as error:
        raise _not_found(error) from error


@router.post(
    "/{product_id}/adjust",
    response_model=MovementResponse,
    status_code=status.HTTP_201_CREATED,
)
def adjust_stock_endpoint(
    product_id: UUID,
    data: StockAdjustment,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("owner")),
):
    try:
        return adjust_stock(db, current_user, product_id, data)
    except ProductNotFoundError as error:
        raise _not_found(error) from error
    except NoStockChangeError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error)) from error
