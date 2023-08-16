from abc import ABC, abstractmethod
from uuid import UUID
from sqlalchemy.orm.exc import NoResultFound



class AbstractRepository(ABC):

    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def get_one():
        raise NotImplementedError

    @abstractmethod
    async def get_all():
        raise NotImplementedError

    @abstractmethod
    async def update():
        raise NotImplementedError

    @abstractmethod
    async def delete():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            one_position = await session.execute(stmt)
            await session.commit()
            return one_position.scalar_one()

    async def get_one(self, id: UUID) -> str:
        async with async_session_maker() as session:
            try:
                stmt = select(self.model.id)
                one_position = await session.execute(stmt)
                return one_position
            except NoResultFound:
                return "Position was not found"

    async def get_all(self):
        async with async_session_maker() as session:
            try:
                stmt = select(self.model)
                all_positions = await session.execute(stmt)
                all_positions = [row[0].to_read_model() for row in all_positions.all()]
                return all_positions
            except NoResultFound:
                return "Positions were not found"

    async def update(self, data: dict) -> str:
        async with async_session_meker as session:
            stmt = self.model.merge_with(**data)
            updated_data = await session.execute(stmt)
            await session.commit()
            return updated_data

    async def delete(self, data: dict) -> str:
        async with async_session_maker as session:
            try:
                stmt = self.model.delete(data)
                deleted_data = await session.execute(stmt)
                await session.commit()
                return deleted_data
            except NoResultFound:
                return "Data was not found"
