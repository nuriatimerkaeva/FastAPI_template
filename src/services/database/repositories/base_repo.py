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
                raise NoResultFound("Position isn't found")


    async def get_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            all_positions = await session.execute(stmt)
            all_positions = [row[0].to_read_model() for row in all_positions.all()]
            return all_positions

    async def update(self, data: dict) -> str:
        async with async_session_meker as session:
            session.merge(data)
            await session.commit()
            return "Updated successfully"

    async def delete(self, data: dict) -> str:
        async with async_session_maker as session:
            try:
                session.delete(data)
                await session.commit()
                return "Deleted successfully"
            except NoResultFound:
                raise NoResultFound("Data isn't found")
