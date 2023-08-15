from typing import Optional
import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import DateTime
from sqlalchemy.orm import mapped_column, Mapped, as_declarative, declared_attr


@as_declarative()
class Base:

    __abstract__: bool = True

    @classmethod
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        attributes = ", ".join(
            f"{attr}={getattr(self, attr)}"
            for attr in self.__mapper__.column_attrs.keys()
        )
        return f"<{class_name}({attributes})>"



class BaseWithIdAndTime:

    id: Mapped[Optional[UUID]] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.now,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.now,
        onupdate=datetime.now,
    )
