from src.interfaces.repository.base_repo import SQLAlchemyRepository
from src.models.user import User


class UserRepository(SQLAlchemyRepository):
    model = User