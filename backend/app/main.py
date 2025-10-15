from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.routers import auth, users, events, health

app = FastAPI(title=settings.app_name, version="1.0.0", openapi_url=f"{settings.api_v1_prefix}/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

prefix = settings.api_v1_prefix

app.include_router(auth.router, prefix=prefix, tags=["Authentication & Access"])
app.include_router(users.router, prefix=prefix, tags=["Authentication & Access"])
app.include_router(events.router, prefix=prefix, tags=["Academic Management"])
app.include_router(health.router, prefix=prefix, tags=["Infrastructure"])
