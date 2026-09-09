from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from . import models
from .schemas import TaskCreate, TaskUpdate


async def create_task(
    db: AsyncSession,
    task_data: TaskCreate
):
    task = models.Task(
        title=task_data.title,
        description=task_data.description,
        completed=False
    )

    db.add(task)

    await db.commit()
    await db.refresh(task)

    return task


async def get_tasks(
    db: AsyncSession,
    skip: int = 0,
    limit: int = 100
):
    statement = (
        select(models.Task)
        .offset(skip)
        .limit(limit)
    )

    result = await db.execute(statement)

    tasks = result.scalars().all()

    return tasks


async def get_task(
    db: AsyncSession,
    task_id: int
):
    statement = (
        select(models.Task)
        .where(models.Task.id == task_id)
    )

    result = await db.execute(statement)

    task = result.scalar_one_or_none()

    return task


async def update_task(
    db: AsyncSession,
    task: models.Task,
    task_data: TaskUpdate
):
    update_data = task_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(task, field, value)

    await db.commit()
    await db.refresh(task)

    return task


async def delete_task(
    db: AsyncSession,
    task: models.Task
):
    await db.delete(task)

    await db.commit()

    return True