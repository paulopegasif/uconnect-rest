from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.utils.deps import get_db, get_current_user
from app.schemas.event import EventCreate, EventRead
from app.repositories import event_repo

router = APIRouter()

@router.get("/events", response_model=list[EventRead], summary="List events (public)")
async def list_events(db: AsyncSession = Depends(get_db)):
    items = await event_repo.list_all(db)
    return items

@router.get("/events/{id}", response_model=EventRead, summary="Get event by id (public)")
async def get_event(id: int, db: AsyncSession = Depends(get_db)):
    obj = await event_repo.get(db, id)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
    return obj

@router.post("/events", response_model=EventRead, status_code=201, summary="Create event")
async def create_event(payload: EventCreate, db: AsyncSession = Depends(get_db), current=Depends(get_current_user)):
    obj = await event_repo.create(db, **payload.dict())
    return obj

@router.put("/events/{id}", response_model=EventRead, summary="Update event")
async def update_event(id: int, payload: EventCreate, db: AsyncSession = Depends(get_db), current=Depends(get_current_user)):
    obj = await event_repo.update(db, id, payload.dict())
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
    return obj

@router.delete("/events/{id}", status_code=204, summary="Delete event")
async def delete_event(id: int, db: AsyncSession = Depends(get_db), current=Depends(get_current_user)):
    ok = await event_repo.remove(db, id)
    if not ok:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
    return None
