from fastapi import FastAPI

from .database import Base, engine
from . import models
from .routers import tasks


app = FastAPI(
    title="Task Management API",
    description="Async Backend Engineering Practice",
    version="2.0.0"
)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(
            Base.metadata.create_all
        )


@app.get("/")
async def root():
    return {
        "message": "Async Task API is running"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }


app.include_router(tasks.router)