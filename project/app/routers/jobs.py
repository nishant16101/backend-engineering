from fastapi import APIRouter, HTTPException
from ..redis import redis_client

router = APIRouter(
    prefix='/jobs',
    tags = ["Jobs"]
)
@router.get("/{job_id}")
async def get_job_status(job_id:str):
    job = await redis_client.hgetall(
        f"job:{job_id}"
    )
    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )
    return job