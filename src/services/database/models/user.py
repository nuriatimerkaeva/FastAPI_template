from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped

from src.services.database.models.base import Base, BaseWithIdAndTime
from src.common.types import _Role


class User(Base, BaseWithIdAndTime):
    name: Mapped[str] = mapped_column(index=True, nullable=True)
    last_name: Mapped[str] = mapped_column(index=True, nullable=True)
    username: Mapped[str] = mapped_column(index=True, nullable=False, unique=True)
    email: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(server_default=False, nullable=False)
    role: Mapped[_Role] = mapped_column(server_default='User', nullable=False)
