from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

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
    task = await crud.get_task(
        db,
        task_id
    )

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


async def update_task(db: AsyncSession,task_id: int,task_data: TaskUpdate
):
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