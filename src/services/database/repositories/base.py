from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm.exc import NoResultFound
from src.services.database.database import async_session_maker
from src.interfaces.repository.abstract_repoitory import AbstractRepository


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            one_position = await session.execute(stmt)
            await session.commit()
            return one_position.scalar_one()

    async def get_one(self, id: UUID):
        async with async_session_maker() as session:
            try:
                stmt = select(self.model).where(self.model.id == id)
                one_position = await session.execute(stmt)
                return one_position.scalar()
            except NoResultFound:
                return "Position was not found"

    async def get_all(self):
        async with async_session_maker() as session:
            try:
                stmt = select(self.model)
                all_positions = await session.execute(stmt)
                return all_positions.scalars().all()
            except NoResultFound:
                return "Positions were not found"

    async def update(self, data: dict):
        async with async_session_maker() as session:
            stmt = (
                update(self.model)
                .where(self.model.id == data['id'])
                .values(**data)
                .returning(self.model)
            )
            updated_data = await session.execute(stmt)
            await session.commit()
            return updated_data.scalar()

    async def delete(self, data: dict):
        async with async_session_maker() as session:
            try:
                stmt = (
                    delete(self.model)
                    .where(self.model.id == data['id'])
                    .returning(self.model)
                )
                deleted_data = await session.execute(stmt)
                await session.commit()
                return deleted_data.scalar()
            except NoResultFound:
                return "Position was not found"