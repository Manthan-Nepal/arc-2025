import json
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any, Dict, List

app = FastAPI()

TASKS_FILE = 'tasks.json'
user_tasks: Dict[str, List[Dict[str, str]]] = {}

def load_tasks():
    global user_tasks
    if not os.path.exists(TASKS_FILE):
        user_tasks = {}
    else:
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            user_tasks = json.load(f)

def save_tasks():
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(user_tasks, f, indent=4)

load_tasks()



class Task(BaseModel):
    task_name: str
    status: str

class UserTask(BaseModel):
    user_name: str
    task: Task

def create_response(success: bool, message: str, data: Any = None) -> Dict[str, Any]:
    response = {"success": success, "message": message}
    if data is not None:
        response["data"] = data
    return response

@app.get("/users")
def list_users():
    users = list(user_tasks.keys())
    if not users:
        return create_response(True, "No users added yet", {"users": []})
    return create_response(True, "Users retrieved successfully", {"users": users})

@app.get("/tasks")
def get_all_tasks():
    if not user_tasks or all(len(tasks) == 0 for tasks in user_tasks.values()):
        return create_response(True, "No tasks added yet", {"tasks": {}})

    return create_response(True, "All user tasks", {"tasks": user_tasks})

@app.get("/tasks/{username}")
def get_user_tasks(username: str):
    tasks = user_tasks.get(username)
    if tasks is None:
        raise HTTPException(status_code=404, detail="User not found")
    return create_response(True, f"Tasks for {username}", {"tasks": tasks})

@app.post("/tasks", status_code=201)
def create_task(user_task: UserTask):
    user = user_task.user_name
    task = user_task.task.model_dump()
    
    user_tasks.setdefault(user, [])

    if any(t["task_name"] == task["task_name"] for t in user_tasks[user]):
        raise HTTPException(status_code=409, detail="Task already exists for this user")
    
    user_tasks[user].append(task)
    save_tasks()
    return create_response(True, "Task added", {"tasks": user_tasks[user]})

@app.put("/tasks/{username}/{task_name}")
def update_task(username: str, task_name: str, task_data: Task):
    tasks = user_tasks.get(username)
    if tasks is None:
        raise HTTPException(status_code=404, detail="User not found")

    for task in tasks:
        if task["task_name"] == task_name:
            task["status"] = task_data.status
            save_tasks()
            return create_response(True, "Task updated", {"tasks": tasks})
    
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{username}/{task_name}")
def delete_task(username: str, task_name: str):
    tasks = user_tasks.get(username)
    if not tasks:
        raise HTTPException(status_code=404, detail="User not found")

    tasks = [task for task in tasks if task["task_name"] != task_name]

    if len(tasks) == len(user_tasks[username]):
        raise HTTPException(status_code=404, detail="Task not found")

    user_tasks[username] = tasks
    save_tasks()
    return create_response(True, "Task deleted", {"remaining_tasks": tasks})

@app.delete("/users/{username}")
def delete_user(username: str):
    if username not in user_tasks:
        raise HTTPException(status_code=404, detail="User not found")

    del user_tasks[username]
    save_tasks()
    
    return create_response(True, f"User '{username}' and all their tasks deleted", {"remaining_users": list(user_tasks.keys())})

