from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from src.services.database.config import POSTGRESQL_DB_URL

engine = create_async_engine(POSTGRESQL_DB_URL, echo=True)

async def get_session(self) -> AsyncSession:
        async with self.sessionmaker as session:
            yield session