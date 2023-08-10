from datetime import date
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped

from src.services.models import Base, BaseWithIdAndTime


class User(Base, BaseWithIdAndTime):

    name: Mapped[str] = mapped_column(index=True, nullable=True)
    last_name: Mapped[str] = mapped_column(index=True, nullable=True)
    username: Mapped[str]  = mapped_column(index=True, nullable=False, unique=True)
    birth_day: Mapped[date] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=False, nullable=False)
    role: Mapped[str] = mapped_column(default='User', nullable=False)