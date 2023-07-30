from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    id: int
    username: str
    hashed_password: str
    email: EmailStr
    role: str
    is_active: bool
    hashed_password: str

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    name: str
    last_name: str
    birth_day: Optional[int]


class UserCreate(UserUpdate):
    pass
