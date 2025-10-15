from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Index
from sqlalchemy.sql import func
from app.db import Base

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    timestamp = Column(DateTime(timezone=True), nullable=False)
    academicGroupId = Column(String(50), nullable=True)
    eventType = Column(String(50), nullable=True, server_default="evento-geral")
    creatorId = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

Index("idx_event_timestamp", Event.timestamp)
Index("idx_event_creator", Event.creatorId)
