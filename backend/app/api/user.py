from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.response import Response
from app.database import get_db
from app.dependencies.auth import get_current_user, get_current_admin
from app.models.user import User
from app.schemas.user import UserUpdateRequest, PasswordUpdateRequest, UserCreateRequest
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

@router.get('/list')
def get_user_page_list(
        page: int = 1,
        page_size: int = 10,
        keywords: str | None = None,
        current_user: User = Depends(get_current_admin),
        db: Session = Depends(get_db)
):
    res = user_service.get_user_list(page, page_size, db, keywords)
    return Response.success(data=res)

@router.post('')
def create_user(
        data: UserCreateRequest,
        current_user: User = Depends(get_current_admin),
        db: Session = Depends(get_db)
):
    res = user_service.create_user(db, data)
    return Response.success(data=res)

@router.put('/{user_id}')
def update_user(
        user_id: int,
        data: UserUpdateRequest,
        current_user: User = Depends(get_current_admin),
        db: Session = Depends(get_db)
):
    res = user_service.admin_update_user(db, user_id, data)
    return Response.success(data=res)

@router.delete('/{user_id}')
def delete_user(user_id: int, current_user: User = Depends(get_current_admin), db: Session = Depends(get_db)):
    user_service.admin_delete_user(db, user_id, current_user)
    return Response.success(message="删除成功！")









