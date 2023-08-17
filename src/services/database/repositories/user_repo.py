from src.services.database.repositories.base_repo import SQLAlchemyRepository
from src.models.user import User


class UserRepository(SQLAlchemyRepository):
    model = User