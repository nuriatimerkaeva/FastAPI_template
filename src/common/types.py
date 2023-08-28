from typing import TypeAlias, Literal, ParamSpec


_Role: TypeAlias = Literal['user', 'admin', 'superuser']
Param = ParamSpec('Param')
EntryType = TypeVar('EntryType')