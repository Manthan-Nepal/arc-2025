from fastapi import APIRouter, HTTPException
from ..dependencies import db_dependency
from ..schemas import Tasks, Updatetask, Taskstatus, Updatetaskstatus, Dailytasks
import models

router= APIRouter(
    tags= ["tasks"],
    responses= {404: {"description": "Not found"}}
    )

@router.get("/tasks")
async def view_tasks(db: db_dependency): #type:ignore    
    return db.query(models.Tasks).all()

@router.get("/tasks/{day}")
async def view_task(day: int, db: db_dependency):  # type: ignore
    task = db.query(models.Tasks).filter(models.Tasks.day == day).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")
    return task

@router.post("/add-task")
async def add_task(task: Tasks, db: db_dependency): #type:ignore
    existing_task = db.query(models.Tasks).filter(models.Tasks.day == task.day).first()
    if existing_task:
        return {"Message": "Task already exists."}    
    new_task= models.Tasks(day= task.day, title= task.title, description= task.description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"message": "New Task Added!"}

@router.get("/daily-tasks")
async def view_daily_tasks(db: db_dependency): #type:ignore    
    return db.query(models.Dailytasks).all()

@router.post("/add-daily-task")
async def add_daily_task(dtask: Dailytasks, db: db_dependency): #type:ignore
    existing_dtask = db.query(models.Dailytasks).filter(models.Dailytasks.day == dtask.day, models.Dailytasks.task_no== dtask.task_no).first()
    if existing_dtask:
        return {"Message": "''{dtask.title}'' daily task already exists."}    
    new_dtask= models.Dailytasks(day= dtask.day, task_no= dtask.task_no, task= dtask.task)
    db.add(new_dtask)
    db.commit()
    db.refresh(new_dtask)
    return {"message": "New Daily Task Added!"}

@router.get("/task-status")
async def view_task_status( db: db_dependency): #type:ignore 
    return db.query(models.Taskstatus).all()
    
@router.post("/add-status")
async def add_task_status(tstatus: Taskstatus, db: db_dependency): #type:ignore
    existing_tstatus = db.query(models.Taskstatus).filter(models.Taskstatus.day == tstatus.day, models.Taskstatus.user_id== tstatus.user_id).first()    
    if existing_tstatus:
        return {"Message": "Task status already exists."}    
    new_tstatus= models.Taskstatus(user_id= tstatus.user_id, status= tstatus.status, day= tstatus.day)    
    db.add(new_tstatus)
    db.commit()
    db.refresh(new_tstatus)
    return {"message": "New Task Status Added!"}

@router.put("/update-task")
async def update_task(task: Updatetask, db: db_dependency): #type:ignore
    existing_task = db.query(models.Tasks).filter(models.Tasks.day == task.day).first()
    if not existing_task:
        return {"Message": "Task doesn't exists."}
    alter_task= models.Tasks(day= task.day, title= task.title, description= task.description)
    if alter_task:        
        db.add(alter_task)
        db.commit()
        db.refresh(alter_task)
        return {"message": "Task {task.day} Updated!"}
    else:
        return {"message": "Invalid entry"}

@router.put("/update-daily-task")
async def update_daily_task(dtask: Dailytasks, db: db_dependency): #type:ignore
    existing_dtask = db.query(models.Dailytasks).filter(models.Dailytasks.day == dtask.day, models.Dailytasks.task_no== dtask.task_no).first()
    if not existing_dtask:
        return {"Message": "Daily task doesn't exists."}    
    alter_dtask= models.Dailytasks(day= dtask.day, task_no= dtask.task_no, task= dtask.task)
    if alter_dtask:        
        db.add(alter_dtask)
        db.commit()
        db.refresh(alter_dtask)
        return {"message": "Task {dtask.task_no} of Day {dtask.day} Updated!"}
    else:
        return {"message": "Invalid entry"}

@router.put("/update-status")
async def update_task_status(tstatus: Updatetaskstatus, db: db_dependency): #type:ignore
    existing_tstatus = db.query(models.Taskstatus).filter(models.Taskstatus.day == tstatus.day, models.Taskstatus.user_id== tstatus.user_id).first()    
    if not existing_tstatus:
        return {"Message": "Task status doesn't exists."}
    alter_tstatus= models.Taskstatus(user_id= tstatus.user_id, status= tstatus.status, day= tstatus.day)
    if alter_tstatus:        
        db.add(alter_tstatus)
        db.commit()
        db.refresh(alter_tstatus)
        return {"message": "Status of Task {tstatus.day} for user {tstatus.user_id} Updated!"}
    else:
        return {"message": "Invalid entry"}