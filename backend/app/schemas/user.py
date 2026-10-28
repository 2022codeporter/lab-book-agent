from typing import Any

from pydantic import BaseModel, ConfigDict

# Pydantic 模型（安全）
class UserResponse(BaseModel):
    id: int
    username: str
    name: str
    role: str
    phone: str | None = None
    email: str | None = None
    avatar: str | None = None
    status: int

    model_config = ConfigDict( from_attributes=True )

class UserCreateRequest(BaseModel):
    username: str # 必填
    password: str = "123"
    name: str # 必填
    phone: str | None = None
    email: str | None = None
    avatar: str | None = None
    role: str = "student"
    status: int = 1

class UserUpdateRequest(BaseModel):
    name: str | None = None
    phone: str | None = None
    email: str | None = None
    avatar: str | None = None
    role: str | None = None
    status: int | None = None

class PasswordUpdateRequest(BaseModel):
    old_password: str
    new_password: str

class PageResponse(BaseModel):
    list: Any = []
    total: int = 0


