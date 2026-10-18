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

        job_id = job["job_id"]

        await update_job_status(
            client,
            job_id,
            "processing"
        )

        try:

            await process_job(job)

            await update_job_status(
                client,
                job_id,
                "completed"
            )

        except Exception as exc:

            print(
                f"Job {job_id} failed: {exc}"
            )

            await update_job_status(
                client,
                job_id,
                "failed"
            )

        await process_job(job)
async def update_job_status(
    client,
    job_id: str,
    status: str
):

    await client.hset(
        f"job:{job_id}",
        "status",
        status
    )


if __name__ == "__main__":
    asyncio.run(worker())