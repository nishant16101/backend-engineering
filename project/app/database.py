import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.ext.asyncio import (create_async_engine,AsyncSession,async_sessionmaker)


#load variables
load_dotenv()

#Read database
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("Database url not configured")

DATABASE_URL = DATABASE_URL.replace(
    "postgresql://",
    "postgresql+asyncpg://",
    1
)

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_size=5,
    max_overflow=10,
    pool_timeout=5
)

#create session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit = False
)

class Base(DeclarativeBase):
    pass

#dependecy for fastapi
async def get_db():
    async with AsyncSessionLocal() as db:
        yield db

