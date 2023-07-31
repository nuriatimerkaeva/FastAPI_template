from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    id: int
    username: str
    hashed_password: str
    email: EmailStr
    role: str
    is_active: bool

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    name: Optional[str]
    last_name: Optional[str]
    birth_day: Optional[int]


class UserCreate(UserBase):
    pass
