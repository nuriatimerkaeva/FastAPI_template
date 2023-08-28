from typing import TypeAlias, Literal, ParamSpec, TypeVar


_Role: TypeAlias = Literal['user', 'admin', 'superuser']
Param = ParamSpec('Param')
EntryType = TypeVar('EntryType')
