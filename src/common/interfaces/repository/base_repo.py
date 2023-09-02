from typing import Protocol, Any
from src.common.types import Param
from abc import abstractmethod


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
