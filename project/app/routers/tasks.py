# app/routers/tasks.py

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

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
def create_task(
    task_data: TaskCreate,
    db: Session = Depends(get_db)
):

    return task_service.create_task(
        db,
        task_data
    )


@router.get(
    "/",
    response_model=list[TaskResponse]
)
def get_tasks(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):

    return task_service.get_all_tasks(
        db,
        skip,
        limit
    )


@router.get(
    "/{task_id}",
    response_model=TaskResponse
)
def get_task(
    task_id: int,
    db: Session = Depends(get_db)
):

    return task_service.get_task_by_id(
        db,
        task_id
    )


@router.put(
    "/{task_id}",
    response_model=TaskResponse
)
def update_task(
    task_id: int,
    task_data: TaskUpdate,
    db: Session = Depends(get_db)
):

    return task_service.update_task(
        db,
        task_id,
        task_data
    )


@router.delete("/{task_id}")
def delete_task(task_id: int,db: Session = Depends(get_db)):

    return task_service.delete_task(
        db,
        task_id
    )

@router.post("/{task_id}/complete")
def complete_task(task_id:int,db:Session=Depends(get_db)):
    task = task_service.get_task_by_id(db,task_id)
    task.complete = True
    db.commit()
    db.refresh()

    return task

@router.post("/{task_id}/increment-priority")
def increment_priority(task_id:int,db:Session=Depends(get_db)):
    task = task_service.get_task_by_id(db,task_id)
    task.priority = task.priority +1
    db.commit()
    db.refresh(task)

    return task
