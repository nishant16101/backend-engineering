# worker/worker.py

import asyncio
import json

import redis.asyncio as redis


REDIS_URL = "redis://localhost:6379"

QUEUE_NAME = "task_queue"


async def process_job(job):

    print(
        f"Processing task "
        f"{job['task_id']}"
    )

    await asyncio.sleep(5)

    print(
        f"Task {job['task_id']} completed"
    )


async def worker():

    client = redis.from_url(
        REDIS_URL,
        decode_responses=True
    )

    print("Worker started")

    while True:

        result = await client.brpop(
            QUEUE_NAME,
            timeout=0
        )

        _, data = result

        job = json.loads(data)

        await process_job(job)


if __name__ == "__main__":
    asyncio.run(worker())