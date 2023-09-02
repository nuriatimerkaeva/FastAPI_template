from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from src.core.settings import settings


engine = create_async_engine(settings.db_url(), echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_session(self) -> AsyncSession:
    async with self.sessionmaker as session:
        yield session