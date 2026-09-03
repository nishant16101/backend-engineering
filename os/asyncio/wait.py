import asyncio
async def worker(name,delay):
    await asyncio.sleep(delay)
    return name

async def main():
    tasks = {
        asyncio.create_task(worker("A",2)),
        asyncio.create_task(worker("B",1)),
        asyncio.create_task(worker("C",3))
    }
    done,pending = await asyncio.wait(tasks)
    for task in done:
        print(task.result())

asyncio.run(main())