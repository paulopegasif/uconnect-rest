from pydantic import BaseModel, Field
from datetime import datetime

class EventBase(BaseModel):
    title: str
    description: str | None = None
    timestamp: datetime
    academicGroupId: str | None = None
    eventType: str | None = Field(default="evento-geral")

class EventCreate(EventBase):
    pass

class EventRead(EventBase):
    id: int
    class Config:
        from_attributes = True
