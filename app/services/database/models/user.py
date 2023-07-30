from sqlalchemy import Column, String, Boolean, Date

from app.services.database.models.base import Base


class User(Base):
    name = Column(String, index=True)
    last_name = Column(String, index=True)
    username = Column(String, index=True, nullable=False, unique=True)
    birth_day = Column(Date, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=False)
    role = Column(String, default='User')