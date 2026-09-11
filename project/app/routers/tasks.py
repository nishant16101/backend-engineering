

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, status,HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import update
from sqlalchemy import select
from ..models import Task
from ..services.external_service import get_post
import time
from ..services.external_service import (
    sequential_requests,
    concurrent_requests
)

from ..database import get_db
from ..schemas import (
    TaskCreate,
    TaskUpdate,
    TaskResponse
)
from ..services import task_service

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post(
    "/",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_task(
    task_data: TaskCreate,
    db: AsyncSession = Depends(get_db)
):
    return await task_service.create_task(
        db,
        task_data
    )


@router.get(
    "/",
    response_model=list[TaskResponse]
)
async def get_tasks(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    return await task_service.get_all_tasks(
        db,
        skip,
        limit
    )


@router.get(
    "/{task_id}",
    response_model=TaskResponse
)
async def get_task(
    task_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await task_service.get_task_by_id(
        db,
        task_id
    )


@router.put(
    "/{task_id}",
    response_model=TaskResponse
)
async def update_task(
    task_id: int,
    task_data: TaskUpdate,
    db: AsyncSession = Depends(get_db)
):
    return await task_service.update_task(
        db,
        task_id,
        task_data
    )


@router.delete(
    "/{task_id}"
)
async def delete_task(
    task_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await task_service.delete_task(
        db,
        task_id
    )

@router.post("/{task_id}/complete")
def complete_task(task_id:int,db:AsyncSession=Depends(get_db)):
    task = task_service.get_task_by_id(db,task_id)
    task.complete = True
    db.commit()
    db.refresh()

    return task

@router.post("/{task_id}/increment-priority")
def increment_priority(task_id:int,db:AsyncSession=Depends(get_db)):
    statement = (
        update(Task).where(Task.id == task_id).values(
            priority = Task.priority +1
        )
    )
    db.execute(statement)
    db.commit()

    task = task_service.get_task_by_id(db,task_id)
    return task


@router.post("/{task_id}/increment-priority-locked")
async def increment_priority_locked(
    task_id: int,
    db: AsyncSession = Depends(get_db)
):

    async with db.begin():

        statement = (
            select(Task)
            .where(Task.id == task_id)
            .with_for_update()
        )

        result = await db.execute(statement)

        task = result.scalar_one_or_none()

        if task is None:
            raise HTTPException(
                status_code=404,
                detail="Task not found"
            )

        task.priority += 1

    return task

@router.get("/pool-test")
def pool_test(db:Session = Depends(get_db)):
    print("Connection acquired")
    time.sleep(10)
    print("Request finished")

    return {
        "message":"Request complete"
    }


@router.post("/{task_id}/transaction-test")
async def transaction_test(task_id:int,db:AsyncSession = Depends(get_db)):
    async with db.begin():
        statement = (select(Task).where(Task.id == task_id))
        result = await db.execute(statement)

        task = result.scalar_one_or_more()
        if task is None:
            raise HTTPException(status_code=404,detail="Task not Found")
        task.priority +=1

    return {
        "message": "Priority updated",
        "task_id": task_id,
        "priority": task.priority
    }

@router.get("/{task_id}/external")
async def external_api_test(task_id:int):
    data = await get_post(task_id)
    return {
        "source":"external_api",
        "data":data
    }

@router.get("/external/sequential")
async def sequential_external():

    return await sequential_requests()

@router.get("/external/concurrent")
async def concurrent_external():

    return await concurrent_requests()

