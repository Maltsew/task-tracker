"""
Организация взаимодейтсвия между базой данных и приложением
"""
import sys
import pathlib

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from .tables import Base

# sys.path.append(pathlib.Path(__file__).resolve().parents[0])
# print(sys.path)


from ..settings import settings

# create engine
db_engine = create_async_engine(settings.database_url, echo=True)

# создание сессии
async_session = sessionmaker(db_engine, expire_on_commit=False, class_=AsyncSession)


async def init_models():
    async with db_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
