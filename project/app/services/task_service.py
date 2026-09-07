from fastapi import HTTPException
from sqlalchemy.orm import Session

from .. import crud
from ..schemas import TaskCreate,TaskUpdate

def create_task(db:Session,task_data:TaskCreate):
    return crud.create_task(
        db,task_data
    )
def get_all_tasks(db:Session,skip:int=0,limit:int=100):
    return crud.get_tasks(db,skip,limit)

def get_task_by_id(db:Session,task_id:int):
    task =  crud.get_task(db,task_id)
    if task is None:
        raise HTTPException(status_code=404,detail="Task not found")
    return task

def update_task(db:Session,task_id:int,task_data:TaskUpdate):
    task = get_task_by_id(
        db,task_id
    )
    return crud.update_task(db,task,task_data)

def delete_task(db:Session,task_id:int):
    task = get_task_by_id(db,task_id)
    crud.delete_task(db,task)
    return {
        "message":"Task deleted sucessfully"
    }