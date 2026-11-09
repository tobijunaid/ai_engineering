from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.business import Business
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password


def register_business_owner(
    db: Session,
    business_name: str,
    user_data: UserCreate,
) -> User:
    
    existing_user = db.scalar(
        select(User).where(User.email == user_data.email)
    )

    if existing_user:
        raise ValueError("Email is already registered.")
    
    try:
        business = Business(
            name=business_name
        )

        db.add(business)
        db.flush()
        #db.flush() sends the business insert to PostgreSQL so its generated ID is available, but doesn't commit the transaction.

        user = User(
            business_id=business.id,
            full_name=user_data.full_name,
            email=user_data.email,
            hashed_password=hash_password(user_data.password),
            role="owner",
            is_active=True,
        )

        db.add(user)
        db.commit()
        #db.commit() saves both the business and user together.
        db.refresh(user)

        return user

    except Exception:
        #db.rollback() cancels the transaction if something fails.
        db.rollback()
        raise