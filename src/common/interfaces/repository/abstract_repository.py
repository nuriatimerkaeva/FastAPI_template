from abc import ABC, abstractmethod
from typing  import Generic, Type, Dict, Iterable, Optional, Any
from src.common.types import EntryType
from src.common.interfaces.repository.base_repo import BaseRepository

class AbstractRepository(ABC, BaseRepository, Generic[EntryType]):

    @abstractmethod
    async def add(self, **values: Dict[str, Any]) -> Optional[EntryType]:
        raise NotImplementedError

    @abstractmethod
    async def get(self, field: Any, value: Any,) -> Optional[EntryType]:
        raise NotImplementedError

    @abstractmethod
    async def update(self, field: Any, value: Any, data: dict) -> Optional[EntryType]:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, field: Any, model_id: int) -> Optional[EntryType]:
        raise NotImplementedError
