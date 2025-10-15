from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: str = Field(default="student")
    active: bool = Field(default=True)

class UserCreate(BaseModel):
    matricula: str
    name: str
    email: EmailStr
    password: str
    role: str = Field(default="student")

class UserRead(UserBase):
    id: int
    class Config:
        from_attributes = True

class UserPatch(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    role: str | None = None
    active: bool | None = None
