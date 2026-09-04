import asyncio

async def worker():
    try:
        print("worker started")
        await asyncio.sleep(10)
        print("worker finishes")
    except asyncio.CancelledError:
        print("worker cancelled")
        raise

async def main():
    task = asyncio.create_task(worker())
    await asyncio.sleep(2)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main detected cancel")


asyncio.run(main())
