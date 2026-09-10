import asyncio
import time
import httpx


URL = "http://127.0.0.1:8000/tasks/"

async def send_request(client,number):
    start = time.perf_counter()
    response = await client.get(URL)

    elapsed = time.perf_counter() - start

    print(f"Request{number}:{response.status_code} {elapsed:2f}s")

    return response

async def main():
    async with httpx.AsyncClient() as client:
        tasks = [send_request(client,i) for i in range(1,11)]
        start = time.perf_counter()

        results= await asyncio.gather(*tasks)
        total = time.perf_counter() - start

        print()
        print(f"Total time: {total:.2f}s")
        print(f"Successful requests: {len(results)}")


if __name__ == "__main__":
    asyncio.run(main())