from pydantic import BaseModel

class LoginRequest(BaseModel):
    matricula: str
    senha: str

class TokenResponse(BaseModel):
    accessToken: str
    tokenType: str = "Bearer"
