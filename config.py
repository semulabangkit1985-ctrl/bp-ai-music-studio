from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    redis_url: str
    storage_dir: str = "/app/storage"
    jwt_secret: str
    cors_origins: str = "http://localhost:3000"

settings = Settings()
