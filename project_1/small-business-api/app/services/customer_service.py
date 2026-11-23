from uuid import UUID

from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.models.customer import Customer
from app.models.user import User
from app.schemas.customer import CustomerCreate, CustomerUpdate


class CustomerNotFoundError(Exception):
    pass


def create_customer(db: Session, user: User, data: CustomerCreate) -> Customer:
    customer = Customer(business_id=user.business_id, **data.model_dump())
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer


def list_customers(db: Session, user: User, search: str | None = None) -> list[Customer]:
    query = select(Customer).where(Customer.business_id == user.business_id)

    if search:
        # ilike = case-insensitive LIKE; % matches any text, so this is "contains".
        pattern = f"%{search}%"
        query = query.where(or_(
            Customer.full_name.ilike(pattern),
            Customer.email.ilike(pattern),
            Customer.phone.ilike(pattern),
        ))

    return list(db.scalars(query.order_by(Customer.full_name)))


def get_customer(db: Session, user: User, customer_id: UUID) -> Customer:
    customer = db.scalar(
        select(Customer).where(
            Customer.id == customer_id,
            Customer.business_id == user.business_id,
        )
    )
    if customer is None:
        raise CustomerNotFoundError("Customer not found.")
    return customer


def update_customer(
    db: Session, user: User, customer_id: UUID, data: CustomerUpdate
) -> Customer:
    customer = get_customer(db, user, customer_id)
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(customer, field, value)
    db.commit()
    db.refresh(customer)
    return customer
