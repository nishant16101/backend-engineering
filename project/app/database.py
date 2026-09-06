import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

#load variables
load_dotenv()

#Read database
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("Database url not configured")

engine = create_engine(
    DATABASE_URL,echo=True
)

#create session factory
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

class Base(DeclarativeBase):
    pass

#dependecy for fastapi
def get_db():
    db = SessionLocal()

    try:
        yield db 
    finally:
        db.close()

