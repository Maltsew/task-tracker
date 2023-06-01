"""
Настройки и переменные окружения
"""
from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    database_url: str = 'postgresql+asyncpg://fastapi:a2095a2095@0.0.0.0:5432/fastapi_app'


settings = Settings(
)



