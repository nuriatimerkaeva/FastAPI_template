from src.services.database.models.user import User
from src.common.dto.user import UserDTO

def user_model_to_dto(user: UserDTO) -> UserDTO:
    return UserDTO(
        id=user.id,
        role=user.role,
        email=user.email,
        username=user.username,
        hashed_password=user.hashed_password,
        is_active=user.is_active,
        name=user.name,
        last_name=user.last_name
    )