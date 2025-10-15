from fastapi import APIRouter
from sqlalchemy import text
from app.db import SessionLocal

router = APIRouter()

@router.get("/health/db", summary="Database connectivity check")
async def db_health():
    async with SessionLocal() as session:
        result = await session.execute(text("SELECT 1"))
        value = result.scalar()
    return {"ok": value == 1}
