from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User

async def create(db: AsyncSession, **data) -> User:
    obj = User(**data)
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

async def get(db: AsyncSession, user_id: int) -> User | None:
    res = await db.execute(select(User).where(User.id == user_id))
    return res.scalar_one_or_none()

async def get_by_matricula(db: AsyncSession, matricula: str) -> User | None:
    res = await db.execute(select(User).where(User.matricula == matricula))
    return res.scalar_one_or_none()

async def list_paginated(db: AsyncSession, page: int, page_size: int):
    offset = (page - 1) * page_size
    res = await db.execute(select(User).offset(offset).limit(page_size))
    items = res.scalars().all()
    total_res = await db.execute(select(User))
    total = len(total_res.scalars().all())
    return {"items": items, "page": page, "pageSize": page_size, "total": total}

async def patch(db: AsyncSession, user_id: int, data: dict) -> User | None:
    res = await db.execute(select(User).where(User.id == user_id))
    obj = res.scalar_one_or_none()
    if not obj:
        return None
    for k, v in data.items():
        setattr(obj, k, v)
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

async def remove(db: AsyncSession, user_id: int) -> bool:
    res = await db.execute(select(User).where(User.id == user_id))
    obj = res.scalar_one_or_none()
    if not obj:
        return False
    await db.delete(obj)
    await db.commit()
    return True
