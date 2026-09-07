from sqlalchemy import select
from sqlalchemy.orm import Session

from . import models
from .schemas import TaskCreate,TaskUpdate

def create_task(db: Session, task_data: TaskCreate):
    task = models.Task(
        title=task_data.title,
        description=task_data.description,
        completed=False
    )

    db.add(task)

    db.commit()

    db.refresh(task)

    return task

def get_tasks(db:Session,skip:int=0,limit:int=100):
    statement = (
        select(models.Task).offset(skip).limit(limit)
    )

    result = db.execute(statement)
    task = result.scalars().all()
    return task

def get_task(db:Session,task_id:int):
    statement = (
        select(models.Task).where(
            models.Task.id == task_id
        )
    )
    result = db.execute(statement)
    task = result.scalar_one_or_none()
    return task


def update_task(db:Session,task:models.Task,task_data:TaskUpdate):
    update_data = task_data.model_dump(
        exclude_unset=True
    )

    for field,value in update_data.items():
        setattr(task,field,value)

    db.commit()
    db.refresh()
    return task


def delete_task(db: Session,task: models.Task):

    db.delete(task)

    db.commit()

    return True

