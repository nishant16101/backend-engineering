import json
from ..redis import redis_client
import uuid

QUEUE_NAME = "task_queue"


async def create_job(task_id:int):
    job_id = str(uuid.uuid4())
    job = {
        "job_id":job_id,
        "task_id":task_id,
        "type":"send_notification",
    }
    await redis_client.hset(
        f"job:{job_id}",
        mapping={
            "job_id": job_id,
            "task_id": str(task_id),
            "type": "send_notification",
            "status": "pending",
        }
    )
    await redis_client.lpush(
        QUEUE_NAME,
        json.dumps(job)
    )
    return job
'''async def enqueue_job(job:dict):
    await redis_client.lpush(QUEUE_NAME,json.dumps(job)) '''

