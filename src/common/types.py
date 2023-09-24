from typing import TypeAlias, Literal, ParamSpec, TypeVar
from src.services.database.models.base import Base


_Role: TypeAlias = Literal['user', 'admin', 'superuser']
Param = ParamSpec('Param')
EntryType = TypeVar('EntryType')
Model = TypeVar('Model', bound=Base)
