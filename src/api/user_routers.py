from fastapi import APIRouter, Depends, HTTPException

from src.services.database.repositories.user_repo import UserRepository
from src.services.database.models.user import User
from src.common.dto.user import UserDTO, UserCreate, UserUpdate
from src.api.dependencies import UserRepositoryDependency

router = APIRouter()


@router.post("/", response_model=UserCreate, status_code=200)
async def create_new_user(new_user: UserCreate,
                          user_crud: UserRepository = Depends(UserRepositoryDependency),
                          ):
    user = await user_crud.get_by_email(email=new_user.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists.",
            )
    user = await user_crud.create_user(new_user)
    return user


@router.get("/{id}/", response_model=UserDTO, status_code=200)
async def get_user_by_id(user: UserDTO,
                         user_crud: UserRepository = Depends(UserRepositoryDependency)
                         ):
    user = await user_crud.get_by_id(id=user.id)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="user does not exist.",
        )
        return user

@router.get("/{email}/", response_model=UserDTO, status_code=200)
async def get_user_by_id(user: UserDTO,
                         user_crud: UserRepository = Depends(UserRepositoryDependency)
                         ):
    user = await user_crud.get_by_email(email=user.email)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="user does not exist.",
        )
        return user
