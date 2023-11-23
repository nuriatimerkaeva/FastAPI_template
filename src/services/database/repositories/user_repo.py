from datetime import timedelta
from fastapi import HTTPException

from typing import ClassVar, Type, Optional, List, Dict
from src.services.database.models.user import User
from src.services.database.repositories.crud import CRUDRepository
from src.common.dto.user import UserDTO, UserCreate, UserUpdate
from src.services.security.security import PasswordManager
from src.services.security.jwt import Auth


class UserRepository(CRUDRepository):
    model: ClassVar[Type[User]] = User

    async def get_user(self, user_id: int = None, email: str = None) -> Optional[UserDTO]:
        if user_id:
            return await self.get(
                field=self.model.id,
                value=user_id
            )
        return await self.get(
            field=self.model.email,
            value=email
        )

    async def create_user(self, data: UserCreate, password_manager: PasswordManager) -> UserDTO:
        new_user_data = data.__dict__
        password = new_user_data.pop('password')
        new_user_data["hashed_password"] = password_manager.encode_password(password)
        return await self.create(new_user_data)

    async def update_user(self, user_id: int, data: UserUpdate) -> UserDTO:
        data = data.__dict__
        return await self.update(
            field=self.model.id,
            value=user_id,
            data=data
        )

    async def get_list_user(self, offset: int = 0, limit: int = 20) -> List[Optional[UserDTO]]:
        return await self.get_many(
            limit=limit,
            offset=offset
        )

    async def authenticate(self, email: str, password: str, password_manager: PasswordManager, auth: Auth) -> Dict[str, str]:
        user = await self.get(email=email)
        if not user or not password_manager.verify_password(password, user.hashed_password):
            raise HTTPException(status_code=404, detail="Incorrect email or password.")
        elif not await self.is_active(user):
            raise HTTPException(status_code=400, detail="Inactive user")
        access_token_expires = timedelta(
            minutes=11520)
        return {
            "access_token": auth.create_access_token(
                data={"user_id": user.id},
                expires_delta=access_token_expires),
            "token_type": "bearer"}

    async def activate_user(self, user_id: int) -> UserDTO:
        data = {'is_active': True}
        return await self.update(
            field=self.model.id,
            value=user_id,
            data=data
        )

    async def password_change(self, user_id: int, new_password: str, password_manager: PasswordManager) -> UserDTO:
        new_password_hash = password_manager.encode_password(new_password)
        data = {"hashed_password": new_password_hash}
        return await self.update(
            field=self.model.id,
            value=user_id,
            data=data
        )

    async def is_active(self, user: UserDTO) -> bool:
        return user.is_active

    async def delete_user(self, user_id: int) -> bool:
        return await self.delete(
            field=self.model.id,
            model_id=user_id)
