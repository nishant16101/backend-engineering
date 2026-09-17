import json
from ..redis import redis_client

QUEUE_NAME = "task_queue"

async def enqueue_job(job:dict):
    await redis_client.lpush(QUEUE_NAME,json.dumps(job))

