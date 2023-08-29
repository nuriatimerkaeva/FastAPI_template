from typing import Protocol
from src.common.types import Param


class BaseRepository(Protocol):

    @abstractmethod
    async def add(self, *args: Param.args, **kwargs: Param.kwargs) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def get(self, *args: Param.args, **kwargs: Param.kwargs) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def update(self, *args: Param.args, **kwargs: Param.kwargs) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, *args: Param.args, **kwargs: Param.kwargs) -> Any:
        raise NotImplementedError
