from typing import Optional
from pydantic import BaseModel, EmailStr
from src.common.types import _Role


class UserDTO(BaseModel):
    id: int
    role: _Role

    class Config:
        from_attributes = True


class UserWithEmail(BaseModel):
    email: EmailStr


class UserPrivate(BaseModel):
    username: str
    hashed_password: str
    is_active: bool


class UserCreate(UserDTO, UserWithEmail, UserPrivate):
    pass


class UserUpdate(BaseModel):
    role: Optional[_Role]
    email: Optional[EmailStr]
    username: Optional[str]
    hashed_password: Optional[str]
    is_active: Optional[bool]
    name: Optional[str]
    last_name: Optional[str]
    birthday: Optional[int]
