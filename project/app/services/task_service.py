from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .cache_service import (get_task_cache,set_task_cache,delete_task_cache)

from .. import crud
from ..schemas import TaskCreate, TaskUpdate


async def create_task(db: AsyncSession,task_data: TaskCreate):
    return await crud.create_task(
        db,
        task_data
    )


async def get_all_tasks(db: AsyncSession,skip: int = 0,limit: int = 100):
    return await crud.get_tasks(
        db,
        skip,
        limit
    )


async def get_task_by_id(db: AsyncSession,task_id: int):
    #check redis
    cached_task = await get_task_cache(task_id)
    if cached_task is not None:
        print("Cache hit")
        return cached_task
    #cache miss
    print("Cache miss")
    task = await crud.get_task(
        db,task_id
    )
    if task is None:
        raise HTTPException(status_code=404,detail="Task Not found")
    
    #convert sqlalchemy object to dict
    task_data = {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed,
        "priority": task.priority
    }
    #store in redis
    await set_task_cache(task_id,task_data)
    #return 
    return task_data

    


async def update_task(db: AsyncSession,task_id: int,task_data: TaskUpdate):
    task = await get_task_by_id(
        db,
        task_id
    )

    return await crud.update_task(
        db,
        task,
        task_data
    )


async def delete_task(db: AsyncSession,task_id: int
):
    task = await get_task_by_id(
        db,
        task_id
    )

    await crud.delete_task(
        db,
        task
    )

    return {
        "message": "Task deleted successfully"
    }