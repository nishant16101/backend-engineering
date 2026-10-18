
import asyncio
import redis.asyncio as redis


async def main():
    client = redis.from_url(
        "redis://localhost:6379",
        encoding="utf-8",
        decode_responses=True,
    )

    try:
        print("PING:", await client.ping())
        print("SET:", await client.set("rate_limit_test", "ok"))
        print("GET:", await client.get("rate_limit_test"))
    except Exception as exc:
        print("ERROR:", repr(exc))
    finally:
        await client.aclose()


asyncio.run(main())
