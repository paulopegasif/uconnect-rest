from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(plain: str) -> str:
    return pwd_context.hash(plain)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

async def authenticate_user(db: AsyncSession, matricula: str, senha: str) -> User | None:
    res = await db.execute(select(User).where(User.matricula == matricula))
    user = res.scalar_one_or_none()
    if not user:
        return None
    if not verify_password(senha, user.password_hash):
        return None
    if not user.active:
        return None
    return user
