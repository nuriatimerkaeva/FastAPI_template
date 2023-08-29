from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.services.database.repositories.user_repo import UserRepository
from src.services.database.models.user import User
from src.common.dto import UserDTO, UserCreate, UserUpdate

router = APIRouter()


@router.post("/create", response_model=UserCreate, status_code=200)
async def create_new_user(new_user: UserCreate,
                          user_crud: UserRepository = Depends(UserRepository),)
    user = await user_crud.get_one(id=user.id)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists.",
            )
    user = await user_crud.add_one(new_user)
    return user


@router.get("/me", response_model=UserDTO, status_code=200)
async def get_user_by_id(user: UserDTO,
                         user_crud: UserRepository = Depends(UserRepository))
    user = await user_crud.get_one(id=user.id)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="user does not exist.",
        )
        return user

@router.put("/update", response_model=UserUpdate, status_code=200)
async def update_user(user: UserUpdate,
                      user_crud: UserRepository = Depends(UserRepository))
    user = await user_crud.update(user)
    return user
