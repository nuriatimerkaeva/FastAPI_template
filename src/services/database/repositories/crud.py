from typing import Type, Dict, Any, Optional, Union, Iterable, Tuple, List
from sqlalchemy.orm import Session
from fastapi import Depends

from src.services.database.session import get_session
from src.common.interfaces.repository.abstract_repository import AbstractRepository
from src.common.interfaces.repository.uow import UnitOfWork
from src.services.database.repositories.base import BaseRepository
from src.common.types import EntryType


class CRUDRepository(AbstractRepository, BaseRepository):

    def __init__(self, model: Type[EntryType], session: Session = Depends(get_session)):
        super().__init__(model)
        self.unit_of_work = UnitOfWork(session)

    async def add_one(self, **values: Dict[str, Any]) -> Optional[EntryType]:
        entry = self.model(**values)
        self.session.add(entry)
        self.unit_of_work.commit()
        self.session.refresh(entry)
        return entry

    async def add_few(self, data: Iterable[Union[EntryType, Dict[str, Any]]]) -> List[EntryType]:
        entries = [self.model(**entry_data) if isinstance(entry_data, dict) else entry_data for entry_data in data]
        self.session.add_all(entries)
        self.unit_of_work.commit()
        self.session.refresh_all(entries)
        return entries

    async def get_one(self, *clauses: Tuple[Any]) -> Optional[EntryType]:
        return self.session.query(self.model).filter(*clauses).first()

    async def get_few(self, *clauses: Tuple[Any], offset: Optional[int], limit: Optional[int]) -> List[EntryType]:
        query = self.session.query(self.model).filter(*clauses)
        if offset is not None:
            query = query.offset(offset)
        if limit is not None:
            query = query.limit(limit)
        return query.all()

    async def update_one(self, *clauses: Tuple[Any], **values: Dict[str, Any]) -> Optional[EntryType]:
        entry = self.get_one(*clauses)
        if entry:
            for key, value in values.items():
                setattr(entry, key, value)
            self.unit_of_work.commit()
            self.session.refresh(entry)
        return entry

    async def update_few(self, data: Iterable[Union[EntryType, Dict[str, Any]]]) -> Any:
        for entry_data in data:
            if isinstance(entry_data, dict):
                entry = self.get_one(*entry_data.get("clauses", ()))
                if entry:
                    for key, value in entry_data.get("values", {}).items():
                        setattr(entry, key, value)
        self.unit_of_work.commit()

    async def delete(self, *clauses: Tuple[Any]) -> Optional[EntryType]:
        entry = self.get_one(*clauses)
        if entry:
            self.session.delete(entry)
            self.unit_of_work.commit()
        return entry
