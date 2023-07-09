from datetime import datetime
from sqlalchemy.ext.declarative import declared_attr, as_declarative
from sqlalchemy import DateTime, Column


@as_declarative
class Base:
    id: int

    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.now,
    )
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.now,
        onupdate=datetime.now,
    )

      @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()