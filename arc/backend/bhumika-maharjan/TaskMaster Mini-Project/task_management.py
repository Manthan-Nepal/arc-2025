import json
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any, Dict

app = FastAPI()

TASKS_FILE = 'tasks.json'
task_list = []

def load_tasks():
    global task_list
    if not os.path.exists(TASKS_FILE):
        task_list = []
    else:
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            task_list = json.load(f)

def save_tasks():
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(task_list, f, indent=4)

def add_task(task):
    if task in task_list:
        return False
    task_list.append(task)
    save_tasks()
    return True

def remove_task(task):
    if task not in task_list:
        return False
    task_list.remove(task)
    save_tasks()
    return True

def get_tasks():
    return task_list

def update_task(task_name: str, new_data: dict):
    for task in task_list:
        if task['task_name'] == task_name:
            task.update(new_data)
            save_tasks()
            return True
    return False

load_tasks()

class Task(BaseModel):
    task_name: str
    status: str

def create_response(success: bool, message: str, data: Any = None) -> Dict[str, Any]:
    response = {
        "success": success,
        "message": message,
    }
    if data is not None:
        response["data"] = data
    return response

@app.get("/tasks")
def read_tasks():
    tasks = get_tasks()
    return create_response(True, "Tasks retrieved successfully", {"tasks": tasks})

@app.post("/tasks", status_code=201)
def create_task(task: Task):
    task_dict = task.model_dump()
    success = add_task(task_dict)
    if not success:
        raise HTTPException(status_code=409, detail="Task already exists")
    return create_response(True, "Task added successfully", {"tasks": get_tasks()})

@app.put("/tasks/{task_name}")
def update_task_endpoint(task_name: str, updated_task: Task):
    if task_name != updated_task.task_name:
        raise HTTPException(status_code=400, detail="Task name cannot be changed")

    success = update_task(task_name, updated_task.model_dump())
    if not success:
        raise HTTPException(status_code=404, detail=f"Task '{task_name}' not found")

    return create_response(True, "Task updated successfully", {"tasks": get_tasks()})

@app.delete("/tasks/{task_name}")
def delete_task(task_name: str):
    success = False
    tasks_to_remove = [t for t in task_list if t["task_name"] == task_name]
    for task in tasks_to_remove:
        if remove_task(task):
            success = True

    if not success:
        raise HTTPException(status_code=404, detail=f"Task '{task_name}' not found")

    return create_response(True, "Task removed successfully", {"tasks": get_tasks()})
