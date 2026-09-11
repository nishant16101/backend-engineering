import asyncio

import redis.asyncio as redis


async def main():

    client = redis.from_url(
        "redis://localhost:6379",
        decode_responses=True
    )

    await client.set(
        "test_key",
        "hello redis"
    )

    value = await client.get("test_key")

    print(value)

    await client.aclose()


if __name__ == "__main__":
    asyncio.run(main())