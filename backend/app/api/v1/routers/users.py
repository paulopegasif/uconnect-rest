from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.utils.deps import get_db, get_current_user
from app.schemas.user import UserCreate, UserRead, UserPatch
from app.repositories import user_repo
from app.services.auth_service import hash_password

router = APIRouter()

@router.get("/users", response_model=dict, summary="List users")
async def list_users(page: int = Query(1, ge=1), pageSize: int = Query(20, ge=1, le=200), db: AsyncSession = Depends(get_db), current=Depends(get_current_user)):
    return await user_repo.list_paginated(db, page, pageSize)

@router.post("/users", response_model=UserRead, status_code=201, summary="Create user")
async def create_user(payload: UserCreate, db: AsyncSession = Depends(get_db), current=Depends(get_current_user)):
    exists = await user_repo.get_by_matricula(db, payload.matricula)
    if exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
    hashed = hash_password(payload.password)
    obj = await user_repo.create(db, matricula=payload.matricula, name=payload.name, email=payload.email, password_hash=hashed, role=payload.role, active=True)
    return obj

@router.get("/users/{id}", response_model=UserRead, summary="Get user by id")
async def get_user(id: int, db: AsyncSession = Depends(get_db), current=Depends(get_current_user)):
    obj = await user_repo.get(db, id)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return obj

@router.patch("/users/{id}", response_model=UserRead, summary="Patch user")
async def patch_user(id: int, payload: UserPatch, db: AsyncSession = Depends(get_db), current=Depends(get_current_user)):
    data = payload.dict(exclude_unset=True)
    obj = await user_repo.patch(db, id, data)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return obj

@router.delete("/users/{id}", status_code=204, summary="Delete user")
async def delete_user(id: int, db: AsyncSession = Depends(get_db), current=Depends(get_current_user)):
    ok = await user_repo.remove(db, id)
    if not ok:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return None


@router.get("/users/me", response_model=UserRead, summary="Current user")
async def users_me(db: AsyncSession = Depends(get_db), current=Depends(get_current_user)):
    obj = await user_repo.get(db, int(current["sub"]))
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return obj
