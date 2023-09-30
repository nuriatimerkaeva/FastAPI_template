from fastapi import APIRouter, Depends, HTTPException
from typing import Any

from src.services.database.repositories.user_repo import UserRepository
from src.services.database.models.user import User
from src.common.dto.user import UserDTO, UserCreate, UserUpdate
from src.api.v1.dependencies import UserRepositoryDependency

router = APIRouter()


@router.post("/", response_model=User)
async def create_user(new_user: UserCreate,
                      user_crud: UserRepository = Depends(UserRepositoryDependency),
                      ) -> Any
    user = await user_crud.get_user_by_email(email=new_user.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = await user_crud.create_user(obj_in=new_user)
    return user


@router.get("/{email}/", response_model=User)
async def get_user(email: str, user_crud: UserRepository = Depends(UserRepositoryDependency)):
    user = await user_crud.get_user_by_email(email)
    return user

@router.get("/{id}/", response_model=User)
async def get_user(id: int, user_crud: UserRepository = Depends(UserRepositoryDependency)):
    user = await user_crud.get_user_by_id(id)
    return user