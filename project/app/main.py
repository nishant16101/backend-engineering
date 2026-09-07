from fastapi import FastAPI
from .database import Base,engine
from .import models
from .routers import tasks

Base.metadata.create_all(
    bind=engine
)

app = FastAPI(
    title="Task management",
    description="Backend engineering practice",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message":"Task Api is running"
    }
@app.get("/health")
def health_check():
    return {
        "status":"healthy"
    }

app.include_router(
    tasks.router
)