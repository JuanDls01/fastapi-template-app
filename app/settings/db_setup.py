from sys import modules

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app import settings


db_connection_url = settings.db_async_connection_url
if "pytest" in modules:
    db_connection_url = settings.db_async_test_connection_url


async_engine = create_async_engine(db_connection_url)
AsyncSessionLocal = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()


# DB Utilities
async def async_get_db():
    async with AsyncSessionLocal() as db:
        yield db
        await db.commit()


from databases import Database

database = Database(db_connection_url)


async def get_db_async_connection():
    await database.connect()
    try:
        yield database
    finally:
        await database.disconnect()
