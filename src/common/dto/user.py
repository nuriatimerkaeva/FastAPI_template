from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from src.common.types import _Role


class UserDTO(BaseModel):
    id: int
    role: _Role
    email: Optional[EmailStr]
    username: Optional[str]
    hashed_password: Optional[str]
    is_active: Optional[bool]
    name: Optional[str] = Field(min_length=1, max_length=128)
    last_name: Optional[str] = Field(min_length=1, max_length=128)

    class Config:
        from_attributes = True


class UserCreate(UserDTO):
    pass


class UserUpdate(BaseModel):
    role: Optional[_Role]
    email: Optional[EmailStr]
    username: Optional[str]
    hashed_password: Optional[str]
    is_active: Optional[bool]
    name: Optional[str] = Field(min_length=1, max_length=128)
    last_name: Optional[str] = Field(min_length=1, max_length=128)
