from sqlalchemy.orm import Session

from app.common.exceptions import BusinessException
from app.models.user import User
from app.schemas.user import UserResponse, UserUpdateRequest, PasswordUpdateRequest
from app.utils.password import verify_pwd, hash_pwd


def get_user(user: User) -> UserResponse:
    return UserResponse.model_validate(user)

def update_user(data: UserUpdateRequest, user: User, db: Session):
    user_dict = data.model_dump(exclude_none=True)
    for field, value in user_dict.items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return UserResponse.model_validate(user)

def update_password(data: PasswordUpdateRequest, user: User, db: Session):
    if not verify_pwd(data.old_password, user.password):
        raise BusinessException(message="原密码错误")
    if data.old_password == data.new_password:
        raise BusinessException(message="新密码不能与原密码相同")
    user.password = hash_pwd(data.new_password)
    db.commit()