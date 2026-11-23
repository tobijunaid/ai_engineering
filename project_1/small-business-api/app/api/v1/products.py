from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import get_current_user, require_role
from app.db.dependencies import get_db
from app.models.user import User
from app.schemas.product import ProductCreate, ProductResponse, ProductUpdate
from app.services.product_service import (
    DuplicateSKUError,
    ProductNotFoundError,
    create_product,
    get_product,
    list_products,
    set_product_active,
    update_product,
)

router = APIRouter(prefix="/products", tags=["Products"])

'''
Permissions (design doc §5):
- Owners and staff can create, view and update products.
- Only owners can deactivate/reactivate products.
Every endpoint is scoped to the current user's business inside the service layer.
'''


@router.post("", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product_endpoint(
    product_data: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        return create_product(db, current_user, product_data)
    except DuplicateSKUError as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(error)) from error


@router.get("", response_model=list[ProductResponse])
def list_products_endpoint(
    include_inactive: bool = False,  # query parameter: /products?include_inactive=true
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return list_products(db, current_user, include_inactive)


@router.get("/{product_id}", response_model=ProductResponse)
def get_product_endpoint(
    product_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        return get_product(db, current_user, product_id)
    except ProductNotFoundError as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error)) from error


@router.patch("/{product_id}", response_model=ProductResponse)
def update_product_endpoint(
    product_id: UUID,
    product_data: ProductUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        return update_product(db, current_user, product_id, product_data)
    except ProductNotFoundError as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error)) from error
    except DuplicateSKUError as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(error)) from error


@router.patch("/{product_id}/deactivate", response_model=ProductResponse)
def deactivate_product_endpoint(
    product_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("owner")),
):
    try:
        return set_product_active(db, current_user, product_id, is_active=False)
    except ProductNotFoundError as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error)) from error


@router.patch("/{product_id}/reactivate", response_model=ProductResponse)
def reactivate_product_endpoint(
    product_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("owner")),
):
    try:
        return set_product_active(db, current_user, product_id, is_active=True)
    except ProductNotFoundError as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error)) from error
