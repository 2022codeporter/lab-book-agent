from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.response import Response
from app.database import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.user import UserUpdateRequest, PasswordUpdateRequest
from app.services import user_service

router = APIRouter(prefix="/api/user", tags=["用户信息接口"])


@router.get("/info")
def get_user_info(current_user: User = Depends(get_current_user)):
    return Response.success(data=user_service.get_user(current_user))

@router.put('/me')
def update_user_info(
        data: UserUpdateRequest,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
    ):
    user = user_service.update_user(data, current_user, db)
    return Response.success(data=user)

@router.put('/password')
def update_user_password(
        data: PasswordUpdateRequest,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    user_service.update_password(data, current_user, db)
    return Response.success(message="修改密码成功！")







