from fastapi import FastAPI, Path
import json
from schemas import Task, Updatetask

app= FastAPI() #uvicorn app_name:app --reload fastapi dev main.py

@app.get("/")
def index():
    return {"This is the root route."}

@app.get("/tasks")
def task_details():
    with open("tasks.json", "r") as tasks_content:
        tasks= json.load(tasks_content)
        return tasks

@app.get("/tasks/{dayx}")
def task_details(dayx: str= Path(description= "Day of Task")): #gt=>, lt<, le<=, ge>=
    with open("tasks.json", "r") as tasks_content:
        tasks= json.load(tasks_content)
        return tasks[dayx]


@app.get("/task-status")
def task_status(status: str):
    getting_status=[]
    with open("tasks.json", "r") as tasks_content:
        tasks= json.load(tasks_content)
        
        for day in tasks:
            if tasks[day]["status"]== status:
                getting_status.append(tasks[day]["title"])
        if getting_status:
            return f"{status} tasks are:", getting_status
        return {"Not Found."}

@app.post("/create-task/{day}")
def create_task(dayx: str, task: Task):
    
    with open("tasks.json", "r+") as tasks_content:
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
        
@app.put("/update-task/{day}")
def update_task(dayx: str, task: Updatetask):
    with open("tasks.json", "r+") as tasks_content:        
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
        



