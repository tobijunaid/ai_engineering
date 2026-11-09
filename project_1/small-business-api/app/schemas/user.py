from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
#UserCreate: Defines the information a user must submit during registration.
class UserCreate(BaseModel):
    business_name: str = Field(min_length=2, max_length=150)
    full_name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


#UserResponse: Defines the information the API returns after registration.
class UserResponse(BaseModel):
    id: UUID
    full_name: str
    email: EmailStr
    role: str
    business_id: UUID
    is_active: bool
    
    model_config = {"from_attributes": True}