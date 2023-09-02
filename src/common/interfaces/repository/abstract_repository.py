from abc import ABC, abstractmethod
from typing  import Generic, Type, Dict, Iterable, Tuple, Optional, Union, Any, List
from src.common.types import EntryType
from src.common.interfaces.repository.base_repo import BaseRepository

class AbstractRepository(ABC, BaseRepository, Generic[EntryType]):

    def __init__(self, model: Type[EntryType]) -> None:
        self.model = model

    @abstractmethod
    async def add_one(self, **values: Dict[str, Any]) -> Optional[EntryType]:
        raise NotImplementedError

    @abstractmethod
    async def add_few(self, data: Iterable[Union[EntryType, Dict[str, Any]]]) -> List[EntryType]:
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, *clauses: Tuple[Any]) -> Optional[EntryType]:
        raise NotImplementedError

    @abstractmethod
    async def get_few(self, *clauses: Tuple[Any], offset: Optional[int], limit: Optional[int]) -> List[EntryType]:
        raise NotImplementedError

    @abstractmethod
    async def update_one(self, *clauses: Tuple[Any], **values: Dict[str, Any]) -> Optional[EntryType]:
        raise NotImplementedError

    @abstractmethod
    async def update_few(self, data: Iterable[Union[EntryType, Dict[str, Any]]]) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, *clauses: Tuple[Any]) -> Optional[EntryType]:
        raise NotImplementedError
