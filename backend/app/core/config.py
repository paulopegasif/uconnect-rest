from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "UCONNECT API"
    api_v1_prefix: str = "/api/v1"
    debug: bool = True

    jwt_secret: str = "replace-this-in-production"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    database_url: str = "postgresql+asyncpg://avnadmin:password@host:24757/defaultdb"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
