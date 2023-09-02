from fastapi import Depends
from typing import Optional, List
from sqlalchemy.orm import Session

from src.services.database.models.user import User
from src.services.database.session import get_session
from src.services.database.repositories.crud import CRUDRepository


class UserRepository(CRUDRepository):
    def __init__(self, session: Session = Depends(get_session)):
        super().__init__(User, session)

    async def find_user_by_username(self, username: str) -> Optional[User]:
        return self.get_one(User.username == username)

    async def find_users_by_role(self, role: str) -> List[User]:
        return self.get_few(User.role == role)
