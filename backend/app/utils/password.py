import bcrypt


def hash_pwd(password: str) -> str:
    """对密码加密"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def verify_pwd(password: str, hashed_password: str) -> bool:
    """验证密码的有效性"""
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))