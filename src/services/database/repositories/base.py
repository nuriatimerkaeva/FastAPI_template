from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from src.services.database.session import get_session


class BaseRepository:
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session