from fastapi import APIRouter, Path, FastAPI, Depends
import json
from ..schemas import Task, Updatetask

router= APIRouter(
    tags= ["tasks"],
    # dependencies= [Depends(Task), Depends(Updatetask)],
    responses= {404: {"description": "Not found"}}
    )

@router.get("/tasks")
async def task_details():
    with open("../files/tasks.json", "r") as tasks_content:
        tasks= json.load(tasks_content)
        return tasks

@router.get("/tasks/{dayx}")
async def task_details(dayx: str= Path(description= "Day of Task")): #gt=>, lt<, le<=, ge>=
    with open("../files/tasks.json", "r") as tasks_content:
        tasks= json.load(tasks_content)
        return tasks[dayx]


@router.get("/task-status")
async def task_status(status: str):
    getting_status=[]
    with open("../files/tasks.json", "r") as tasks_content:
        tasks= json.load(tasks_content)
        
        for day in tasks:
            if tasks[day]["status"]== status:
                getting_status.append(tasks[day]["title"])
        if getting_status:
            return f"{status} tasks are:", getting_status
        return {"Not Found."}

@router.post("/create-task/{day}", response_model=Task)
async def create_task(dayx: str, task: Task):
    
    with open("../files/tasks.json", "r+") as tasks_content:
        tasks= json.load(tasks_content)
        
        if dayx in tasks:
            return {"Task of that day already exists."}    
                       
        tasks[dayx]={
            "title": task.title,
            "status": task.status            
        }
        tasks_content.seek(0)
        json.dump(tasks, tasks_content, indent=4)
        tasks_content.truncate()
        return tasks[dayx]
        
@router.put("/update-task/{day}", response_model= Updatetask)
async def update_task(dayx: str, task: Updatetask):
    with open("../files/tasks.json", "r+") as tasks_content:        
        update= json.load(tasks_content)
        
        if dayx not in update:
            return {"Task Day not found."}
        
        if task.title != None:
            update[dayx]["title"]= task.title       
        if task.status != None:
            update[dayx]["status"]= task.status
 
        tasks_content.seek(0)
        json.dump(update, tasks_content, indent=4)
        tasks_content.truncate()
        
    return update[dayx]