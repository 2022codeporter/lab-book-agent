from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.common.response import Response
from app.database import get_db
from app.schemas.auth import LoginRequest, LoginResponse, RegisterRequest
from app.services import auth_service




router = APIRouter(prefix="/api/auth", tags=["权限验证"])



@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    result = auth_service.login(data, db)

    # 返回信息
    return Response.success(
        message="登录成功！",
        data=result
    )

@router.post("/register")
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    auth_service.register(data, db)
    return Response.success(message="注册成功！")













