from typing import Optional
from pydantic import BaseModel, EmailStr


class UserDTO(BaseModel):
    id: int
    role: str

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


class UserUpdate(UserCreate):
    name: Optional[str]
    last_name: Optional[str]
    birth_day: Optional[int]
