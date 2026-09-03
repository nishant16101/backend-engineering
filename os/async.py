import asyncio

async def task1():
    print("A")
    await asyncio.sleep(2)
    print("B")

async def task2():
    print("C")
    await asyncio.sleep(2)
    print("D")

async def main():
    await asyncio.gather(
        task1(),
        task2()
    )

asyncio.run(main())