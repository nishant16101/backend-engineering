from fastapi import HTTPException,Request
from redis.asyncio import Redis
import hashlib

RATE_LIMIT = 5
WINDOW_SECONDS = 60


redis_client = Redis.from_url(
    "redis://localhost:6379",
    encoding="utf-8",
    decode_responses=True,
)



RATE_LIMIT_SCRIPT = """
local count = redis.call('INCR', KEYS[1])

if count == 1 then
    redis.call('EXPIRE', KEYS[1], tonumber(ARGV[1]))
end

local ttl = redis.call('TTL', KEYS[1])

return {count, ttl}
"""


async def rate_limit(request:Request)->None:
    client_host = (request.client.host if request.client else "unknown")
    client_id = hashlib.sha256(client_host.encode()).hexdigest()

    key = f"rate_limit:{client_id}"
    try:
        result = await redis_client.eval(RATE_LIMIT_SCRIPT,1,key,WINDOW_SECONDS)
    
    except Exception as exc:
        import traceback
        traceback.print_exc()

        raise HTTPException(
            status_code=503,
            detail="Rate-limiting service unavailable",
        )

    count,ttl = int(result[0]),int(result[1])

    if count > RATE_LIMIT:
        raise HTTPException(
            status_code=429,detail="Rate limited exceeded. Try again later",
            headers={"Retry-After": str(max(ttl, 1))},
        )