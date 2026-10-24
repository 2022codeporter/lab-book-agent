
from datetime import timedelta, datetime

import jwt
from app.config import settings

def create_access_token(user_id: int) -> str:
    """创建 jwt token
    :rtype: sstr    """
     expire = datetime.now() + timedelta(hours=settings.JWT_EXPIRE_HOURS)

     payload = {"user_id": user_id, "exp": expire}

     return jwt.encode(payload=payload, key=settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def decode_access_token(token: str) -> dict:
    """解析 jwt token"""
    return jwt.decode(token, key=settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])