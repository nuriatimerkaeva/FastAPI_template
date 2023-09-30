from typing import ClassVar, Type, Optional
from src.services.database.models.user import User
from src.services.database.repositories.base import BaseRepository
from src.common.dto.user import UserDTO, UserCreate, UserUpdate, UserWithEmail, UserPrivate
from src.services.security.security import PasswordManager

class UserRepository(BaseRepository):
    model: ClassVar[Type[User]] = User

    async def get_user_by_id(self, user_id: int = None) -> Optional[UserDTO]:
        return await self._crud_repo.get(field=self.model.id, value=user_id)

    async def get_user_by_email(self, email: str = None) -> Optional[UserWithEmail]:
        return await self._crud_repo.get(field=self.model.email, value=email)

    async def create_user(self, data: UserCreate) -> Optional[UserCreate]:
        new_user = data.__dict__
        password = new_user.pop('password')
        new_user["hashed_password"] = PasswordManager.encode_password(password)
        return await self._crud_repo.create(new_user)

    async def update_user(self,user_id: int, data: UserUpdate) -> Optional[UserUpdate]:
        data = data.__dict__
        return await self._crud_repo.update(field=self.model.id, value=user_id, data=data)

    async def delete_user(self, user_id: int) -> bool:
        return await self._crud_repo.delete(field=self.model.id, model_id=user_id)