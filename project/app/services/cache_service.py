import json
from ..redis import redis_client
TASK_TTL = 60

async def get_task_cache(task_id:int):
    key = f"task:{task_id}"
    data = await redis_client.get(key)
    if data is None:
        return None

    return json.loads(data)

async def set_task_cache(task_id:int,task_data:dict):
    key = f"task:{task_id}" 
    await redis_client.set(key,json.dumps(task_data),ex=TASK_TTL)


async def delete_task_cache(task_id:int):
    key = f"task:{task_id}"
    await redis_client.delete(key)
