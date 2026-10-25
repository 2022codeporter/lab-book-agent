from sqlalchemy.orm import Session
from app.common.exceptions import BusinessException
from app.schemas.auth import LoginRequest, LoginResponse, RegisterRequest
from app.models.user import User
from app.schemas.user import UserResponse
from app.utils.password import verify_pwd, hash_pwd
from app.utils.jwt import create_access_token



def login(data: LoginRequest, db: Session):
    # 根据用户账号查询数据库
    user = db.query(User).filter(User.username == data.username).first()

    # 判断账号和密码是否正确
    if not user or not verify_pwd(data.password, user.password):
        raise BusinessException(message="账号或密码错误")

    # 验证账号的状态
    if int(user.status) != 1:
        raise BusinessException(message="账号已被禁用")

    # 创建token
    token = create_access_token(user.id)

    return LoginResponse(token=token, user=UserResponse.model_validate(user))

def register(data: RegisterRequest, db: Session):
    is_exist = db.query(User).filter(User.username == data.username).first()
    if is_exist:
        raise BusinessException(message="该用户名已存在！")
    user = User(
        username=data.username,
        password=hash_pwd(data.password),
        name=data.name or data.username,
        role="student",
        status=1
    )
    db.add(user)
    db.commit()
    db.refresh(user)






