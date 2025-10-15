from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.auth import LoginRequest, TokenResponse
from fastapi import Body
from app.core.security import create_access_token
from app.services.auth_service import authenticate_user
from app.utils.deps import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.post("/auth/login", response_model=TokenResponse, summary="Login and create session")
@router.post("/auth/login", response_model=TokenResponse, summary="Login and create session")
async def login(body: dict = Body(...), db: AsyncSession = Depends(get_db)):
    matricula = body.get("matricula") or body.get("registration")
    senha = body.get("senha") or body.get("password")
    if not matricula or not senha:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing credentials")
    user = await authenticate_user(db, matricula, senha)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials or inactive user")
    token = create_access_token(sub=str(user.id), role=user.role)
    # return both keys to be compatible with different frontends
    return {"accessToken": token, "tokenType": "Bearer", "access_token": token, "token_type": "Bearer"}
@router.post("/auth/logout", summary="Logout (client-side token discard)")
async def logout():
    return {"ok": True}

@router.get("/auth/validate", summary="Validate token")
async def validate():
    return {"valid": True}