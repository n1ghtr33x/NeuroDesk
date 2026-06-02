from pydantic_settings import BaseSettings
from .settings import (
    JWT_SECRET, 
    JWT_ALGORITHM, 
    ACCESS_TOKEN_EXPIRE_MINUTES, 
    DATABASE_URL,
    AI_API_KEY,
    AI_BASE_URL,
    DEFAULT_MODEL
    )

class Settings(BaseSettings):
    SECRET_KEY: str = JWT_SECRET
    ALGORITHM: str = JWT_ALGORITHM
    ACCESS_TOKEN_EXPIRE_MINUTES: int = ACCESS_TOKEN_EXPIRE_MINUTES
    DATABASE_URL: str = DATABASE_URL
    AI_API_KEY: str = AI_API_KEY
    AI_BASE_URL: str = AI_BASE_URL
    DEFAULT_MODEL: str = DEFAULT_MODEL

settings = Settings()
