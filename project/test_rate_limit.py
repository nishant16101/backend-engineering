
import asyncio
import redis.asyncio as redis

SCRIPT = """
local count = redis.call('INCR', KEYS[1])

if count == 1 then
    redis.call('EXPIRE', KEYS[1], ARGV[1])
end

local ttl = redis.call('TTL', KEYS[1])
return {count, ttl}
"""


async def main():
    client = redis.from_url(
        "redis://localhost:6379",
        encoding="utf-8",
        decode_responses=True,
    )

    try:
        result = await client.eval(
            SCRIPT,
            1,
            "rate_limit:diagnostic_test",
            60,
        )
        print("RATE LIMIT SCRIPT RESULT:", result)
    except Exception as exc:
        print("SCRIPT ERROR:", repr(exc))
    finally:
        await client.aclose()


asyncio.run(main())
