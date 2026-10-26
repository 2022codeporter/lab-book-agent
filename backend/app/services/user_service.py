from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserResponse, UserUpdateRequest


def get_user(user: User) -> UserResponse:
    return UserResponse.model_validate(user)

def update_user(data: UserUpdateRequest, user: User, db: Session):
    user_dict = data.model_dump(exclude_none=True)
    for field, value in user_dict.items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return UserResponse.model_validate(user)