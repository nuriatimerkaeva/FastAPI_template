from fastapi import APIRouter, Depends, HTTPException
from typing import Any, Dict, Union

from src.services.database.repositories.user_repo import UserRepository
from src.services.database.models.user import User
from src.common.dto.user import UserDTO, UserCreate, UserUpdate
from src.api.v1.dependencies import UserRepositoryDependencyMarker

router = APIRouter()


@router.post("/", response_model=User)
async def create_user(user_in: UserCreate, user_crud: UserRepository = Depends(UserRepositoryDependencyMarker)) -> UserDTO:
    user = await user_crud.get_by_email(email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = await user_crud.create_user(obj_in=user_in)
    return user


@router.put('/update/{user_id}')
async def update_user(user_id: int, data: UserUpdate, current_user: UserDTO, user_crud: UserRepository = Depends(UserRepositoryDependencyMarker)) -> UserDTO:
    return await user_crud.update_user(user_id=user_id, data=data)


@router.delete('/delete/{user_id}')
async def delete_user(user_id: int, current_user: UserDTO, user_crud: UserRepository = Depends(UserRepositoryDependencyMarker)) -> Dict[str, str]:
    result = await user_crud.delete_user(user_id=user_id)
    if result:
        return {"message": "user successfully deleted"}
    raise HTTPException(404, "user does not exists")
