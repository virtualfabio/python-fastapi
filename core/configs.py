from typing import List

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://geek:123456@localhost:5432/teste01db'
    DBBaseModel = declarative_base()

    JWT_SECRET: str = 'ciIqKZgIYekxZq9FMhNzVTrZEyms8vse73T7hmqYJ2M'
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # = 1 semana em minutos

    class Config:
        case_sensetive = True


settings: Settings = Settings()
