from operator import or_

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.common.exceptions import BusinessException
from app.models.user import User
from app.schemas.user import UserResponse, UserUpdateRequest, PasswordUpdateRequest, PageResponse, UserCreateRequest
from app.utils.password import verify_pwd, hash_pwd


def get_user(user: User) -> UserResponse:
    return UserResponse.model_validate(user)

def update_user(data: UserUpdateRequest, user: User, db: Session):
    user_dict = data.model_dump(exclude_none=True, exclude={"role", "status"})
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

def get_user_list(page: int, page_size: int, db: Session, keywords: str | None = None):
    query = db.query(User)
    if keywords:
        query = query.filter(
            or_(User.username.ilike(f"%{keywords}%"), User.name.ilike(f"%{keywords}%"))
        )
    total = query.count()
    items = (
        query.order_by(User.id.desc())
        .offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )

    return PageResponse(
        list=[UserResponse.model_validate(item) for item in items], total=total
    )

def create_user(db: Session, data: UserCreateRequest):
    stmt = select(User).where(User.username == data.username)
    res = db.execute(stmt).scalar_one_or_none()
    if res is not None:
        raise BusinessException(message="账号已存在！")

    user = User(
        username=data.username,
        password=hash_pwd(data.password),
        name=data.name,
        role=data.role,
        email=data.email,
        phone=data.phone,
        avatar=data.avatar,
        status=data.status
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return UserResponse.model_validate(user)

def admin_update_user(db: Session, user_id: int, data: UserUpdateRequest):
    stmt = select(User).where(User.id == user_id)
    user = db.execute(stmt).scalar_one_or_none()
    if not user:
        raise BusinessException(message="用户不存在！")
    payload = data.model_dump(exclude_none=True)
    for field, value in payload.items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return UserResponse.model_validate(user)


def admin_delete_user(db: Session, user_id: int, current_user: User):
    if user_id == current_user.id:
        raise BusinessException(message="不能删除当前账号")
    stmt = select(User).where(User.id == user_id)
    user = db.execute(stmt).scalar_one_or_none()
    if not user:
        raise BusinessException(message="用户不存在！")
    db.delete(user)
    db.commit()












