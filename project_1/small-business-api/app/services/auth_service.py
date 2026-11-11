from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.business import Business
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password
from app.core.security import verify_password, create_access_token
from app.schemas.user import UserLogin


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


'''
What this function below does
1. Finds the user using their email.
2. Verifies their password.
3. Checks whether their account is active.
4. Generates a JWT containing their user UUID.
5. Returns the access token.
'''
def login_user(db: Session, login_data: UserLogin) -> dict:
    user = db.scalar(
        select(User).where(User.email == login_data.email)
    )

    if not user:
        raise ValueError("Invalid email or password.")

    if not verify_password(
        login_data.password,
        user.hashed_password
    ):
        raise ValueError("Invalid email or password.")

    if not user.is_active:
        raise ValueError("This account is inactive.")

    access_token = create_access_token(
        data={"sub": str(user.id)}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }