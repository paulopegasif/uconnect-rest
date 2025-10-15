from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.event import Event

async def list_all(db: AsyncSession):
    res = await db.execute(select(Event).order_by(Event.timestamp.desc()))
    return res.scalars().all()

async def get(db: AsyncSession, event_id: int):
    res = await db.execute(select(Event).where(Event.id == event_id))
    return res.scalar_one_or_none()

async def create(db: AsyncSession, **data):
    obj = Event(**data)
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

async def update(db: AsyncSession, event_id: int, data: dict):
    obj = await get(db, event_id)
    if not obj:
        return None
    for k, v in data.items():
        setattr(obj, k, v)
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

async def remove(db: AsyncSession, event_id: int) -> bool:
    obj = await get(db, event_id)
    if not obj:
        return False
    await db.delete(obj)
    await db.commit()
    return True
