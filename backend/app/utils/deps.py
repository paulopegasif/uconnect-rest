from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession
from jose import jwt, JWTError

from app.core.config import settings
from app.db import SessionLocal

security = HTTPBearer()

async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session

async def get_current_user(creds: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    token = creds.credentials
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
        return {"sub": payload.get("sub"), "role": payload.get("role")}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
