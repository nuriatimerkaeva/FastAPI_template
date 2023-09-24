from abc import ABC
from typing import ClassVar, Type
from sqlalchemy.ext.asyncio import AsyncSession

from src.services.database.repositories.crud import CRUDRepository
from src.common.types import Model



class BaseRepository(ABC):
    model: ClassVar[Type[Model]]

    def __init__(self, session: AsyncSession):
        self._session = session
        self._crud_repo = CRUDRepository(session, self.model)
