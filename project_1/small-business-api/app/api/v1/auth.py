from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID
from fastapi.security import OAuth2PasswordRequestForm
from app.models.user import User
from app.core.security import get_current_user, require_role
from app.db.dependencies import get_db
from app.schemas.user import UserCreate, UserResponse, UserLogin, TokenResponse, StaffCreate
from app.services.auth_service import (
    register_business_owner,
    login_user,
    create_staff,
    get_business_staff,
    deactivate_staff,
    reactivate_staff
)

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    try:
        user = register_business_owner(
            db=db,
            business_name=user_data.business_name,
            user_data=user_data,
        )
        return user
    
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        ) from error
        
        
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Registration failed. Check that the email is not already registered.",
        ) from error

@router.post("/login", response_model=TokenResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    login_data = UserLogin(
        email=form_data.username,
        password=form_data.password,
    )

    try:
        return login_user(db, login_data)

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(error),
            headers={"WWW-Authenticate": "Bearer"},
        ) from error
        

@router.get("/me", response_model=UserResponse)
def get_me(
    current_user: User = Depends(get_current_user),
):
    return current_user

@router.get("/owner-check")
def owner_check(
    current_user: User = Depends(require_role("owner")),
):
    return {
        "message": "Owner access granted.",
        "user": current_user.full_name,
        "role": current_user.role,
    }
    
'''
This endpoint below:
- Requires an authenticated owner.
- Automatically assigns the owner's business_id to the staff member.
- Assigns the staff role.
- Returns 409 Conflict if the email already exists.
'''
@router.post(
    "/staff",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register_staff(
    staff_data: StaffCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("owner")),
):
    try:
        staff = create_staff(
            db=db,
            owner=current_user,
            staff_data=staff_data,
        )
        return staff

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        ) from error

'''
What this endpoint below does
- GET /api/v1/auth/staff retrieves staff members.
- Only users with the owner role can access it.
- It returns staff belonging to the authenticated owner's business.
- It does not expose staff belonging to other businesses.
'''

@router.get("/staff", response_model=list[UserResponse])
def list_staff(
    current_user: User = Depends(require_role("owner")),
    db: Session = Depends(get_db),
):
    return get_business_staff(db, current_user)

@router.patch("/staff/{staff_id}/deactivate", response_model=UserResponse)
def deactivate_staff_member(
    staff_id: UUID,
    current_user: User = Depends(require_role("owner")),
    db: Session = Depends(get_db),
):
    try:
        return deactivate_staff(db, current_user, staff_id)
    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error),
        )

@router.patch(
    "/staff/{staff_id}/reactivate",
    response_model=UserResponse,
)
def reactivate_staff_member(
    staff_id: UUID,
    current_user: User = Depends(require_role("owner")),
    db: Session = Depends(get_db),
):
    try:
        return reactivate_staff(db, current_user, staff_id)
    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error),
        )

