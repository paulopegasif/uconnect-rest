from datetime import datetime, timedelta
from jose import jwt
from typing import Optional
from app.core.config import settings

def create_access_token(sub: str, role: str, expires_minutes: Optional[int] = None) -> str:
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes or settings.access_token_expire_minutes)
    payload = {"sub": sub, "role": role, "exp": expire, "iat": datetime.utcnow()}
    return jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)
