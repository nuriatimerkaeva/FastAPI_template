from typing import ClassVar, Type
from src.services.database.models.user import User
from src.services.database.repositories.base import BaseRepository
from src.common.dto.user import UserDTO, UserCreate, UserUpdate, UserWithEmail, UserPrivate


class UserRepository(BaseRepository):
    model: ClassVar[Type[User]] = User

    async def get_by_id(self, user_id: int) -> UserDTO:
        user = await self._get(User.id, user_id)
        return UserDTO.model_validate(user) if user else None

    async def get_by_email(self, email: str) -> UserWithEmail:
        user = await self._get(User.email, email)
        return UserWithEmail.model_validate(user) if user else None

    async def create_user(self, user_create: UserCreate) -> UserPrivate:
        user = await self._add(**user_create.model_dump())
        return UserPrivate.model_validate(user)

    async def update_user(self, user_id: int, user_update: UserUpdate) -> UserUpdate:
        user = await self._update(User.id, user_id, user_update.model_dump(exclude_unset=True))
        return UserUpdate.model_validate(user)

    async def delete_user(self, user_id: int) -> UserDTO:
        user = await self._delete(User.id, user_id)
        return UserPrivate.model_validate(user)