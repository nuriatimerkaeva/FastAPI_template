from typing import ClassVar, Type, Any, Optional, Dict
from sqlalchemy import select, update, delete, insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.exc import NoResultFound

from src.common.interfaces.repository.abstract_repository import AbstractRepository
from src.common.types import Model


class CRUDRepository(AbstractRepository):

    model: ClassVar[Type[Model]]

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: dict) -> Optional[Model]:
        new_obj = self.model(**data)
        self.session.add(new_obj)
        await self.session.commit()
        await self.session.refresh(new_obj)
        return new_obj

    async def get(self, field: Any, value: Any) -> Optional[Model]:
        try:
            stmt = (select(self.model)
                    .where(field == value)
                    )
            return (await self.session.execute(stmt)).scalars().first()
        except NoResultFound:
            return None

    async def update(self, field: Any, value: Any, data: dict) -> Optional[Model]:
        stmt = (
            update(self.model)
            .where(field == value)
            .values(**data)
            .returning(self.model)
        )
        return (await self.session.execute(stmt)).scalars().all()

    async def delete(self, field: Any, model_id: int) -> Optional[Model]:
        stmt = (
            delete(self.model)
            .where(field == model_id)
            .returning(self.model)
        )
        return (await self.session.execute(stmt)).scalars().all()
