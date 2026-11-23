from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.db.dependencies import get_db
from app.models.user import User
from app.schemas.customer import CustomerCreate, CustomerResponse, CustomerUpdate
from app.schemas.invoice import InvoiceResponse
from app.services.invoice_service import list_invoices
from app.services.customer_service import (
    CustomerNotFoundError,
    create_customer,
    get_customer,
    list_customers,
    update_customer,
)

router = APIRouter(prefix="/customers", tags=["Customers"])

'''
Owners and staff can manage customers (design doc §5).
There is no delete endpoint: the design doesn't call for one, and invoices
reference customers, so removing them would break invoice history.
'''


@router.post("", response_model=CustomerResponse, status_code=status.HTTP_201_CREATED)
def create_customer_endpoint(
    data: CustomerCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_customer(db, current_user, data)


@router.get("", response_model=list[CustomerResponse])
def list_customers_endpoint(
    search: str | None = None,  # /customers?search=ade  matches name, email or phone
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return list_customers(db, current_user, search)


@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer_endpoint(
    customer_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        return get_customer(db, current_user, customer_id)
    except CustomerNotFoundError as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error)) from error


@router.patch("/{customer_id}", response_model=CustomerResponse)
def update_customer_endpoint(
    customer_id: UUID,
    data: CustomerUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        return update_customer(db, current_user, customer_id, data)
    except CustomerNotFoundError as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error)) from error


@router.get("/{customer_id}/invoices", response_model=list[InvoiceResponse])
def customer_invoice_history(
    customer_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        get_customer(db, current_user, customer_id)  # 404 if not in this business
    except CustomerNotFoundError as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error)) from error
    return list_invoices(db, current_user, customer_id=customer_id)
