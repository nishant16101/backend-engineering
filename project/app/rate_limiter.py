from fastapi import HTTPException,Request,Response
from redis.asyncio import Redis
import hashlib
import os

RATE_LIMIT = 5
WINDOW_SECONDS = 60


redis_client = Redis.from_url(
    os.getenv("REDIS_URL", "redis://localhost:6379"),
    encoding="utf-8",
    decode_responses=True,
)


RATE_LIMIT_SCRIPT = """
local count = redis.call('INCR', KEYS[1])

if count == 1 or redis.call('TTL', KEYS[1]) == -1 then
    redis.call('EXPIRE', KEYS[1], tonumber(ARGV[1]))
end

local ttl = redis.call('TTL', KEYS[1])

return {count, ttl}
"""


async def rate_limit(
    request: Request,
    response: Response,
) -> None:
    client_host = (
        request.client.host if request.client else "unknown"
    )

    client_id = hashlib.sha256(
        client_host.encode()
    ).hexdigest()

    key = f"rate_limit:{client_id}"

    try:
        result = await redis_client.eval(
            RATE_LIMIT_SCRIPT,
            1,
            key,
            WINDOW_SECONDS,
        )
    except Exception:
        # Log details on the server; don't expose them to clients.
        import logging
        logging.getLogger(__name__).exception(
            "Redis rate limiter failed"
        )
        raise HTTPException(
            status_code=503,
            detail="Rate-limiting service unavailable",
        )

    count, ttl = int(result[0]), int(result[1])
    remaining = max(0, RATE_LIMIT - count)

    headers = {
        "X-RateLimit-Limit": str(RATE_LIMIT),
        "X-RateLimit-Remaining": str(remaining),
    }

    if count > RATE_LIMIT:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded. Try again later.",
            headers={
                **headers,
                "Retry-After": str(max(ttl, 1)),
            },
        )

    response.headers.update(headers)