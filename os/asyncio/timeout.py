import asyncio
async def slow_api():
    await asyncio.sleep(5)
    return "success"

async def main():
    try:
        async with asyncio.timeout(1):
            result = await slow_api()
            print(result)

    except TimeoutError:
        print("Request timed out")
asyncio.run(main())