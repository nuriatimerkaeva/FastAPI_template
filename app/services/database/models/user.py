from sqlalchemy import Column, Integer, String, Boolean, VARCHAR, Date

from app.services.database.models.base import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(50), index=True)
    last_name = Column(VARCHAR(50), index=True)
    username = Column(VARCHAR(30), index=True, nullable=False, unique=True)
    birth_day = Column(Date, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)