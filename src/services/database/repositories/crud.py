from typing import ClassVar, Type, Any, Optional, List
from sqlalchemy import select, update, delete, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.common.interfaces.repository.abstract_repository import AbstractRepository
from src.common.types import Model


class CRUDRepository(AbstractRepository):

    model: ClassVar[Type[Model]]

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get(self, field: Any, value: Any) -> Optional[Model]:

        stmt = (
            select(self.model)
            .where(field == value)
        )

        result = await self._session.scalar(stmt)
        return result

    async def create(self, data: dict) -> Model:
        new_obj = self.model(**data)
        self._session.add(new_obj)
        await self._session.commit()
        await self._session.refresh(new_obj)
        return new_obj

    async def update(self, field: Any, value: Any, data: dict) -> Model:
        stmt = (
            update(self.model)
            .where(field == value)
            .values(**data)
            .returning(self.model)
        )
        result = await self._session.scalar(stmt)
        await self._session.commit()
        await self._session.refresh(result)
        return result

    async def delete(self, field: Any, model_id: int) -> Optional[bool]:
        stmt = (
            delete(self.model)
            .where(field == model_id)
        )

        result = await self._session.execute(stmt)
        await self._session.commit()
        if result.rowcount:
            return True
        return None

    async def get_many(self, limit: int, offset: int, field: Any = None, value: Any = None) -> Optional[List[Model]]:

        if field and value:
            stmt = (
                select(self.model)
                .where(field == value)
                .offset(offset)
                .limit(limit)
            )
        else:
            stmt = (
                select(self.model)
                .offset(offset)
                .limit(limit)
            )
        result = await self._session.scalars(stmt)
        return result.all()
