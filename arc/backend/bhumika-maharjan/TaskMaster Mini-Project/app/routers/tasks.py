from fastapi import APIRouter, HTTPException
from app.models import Task, UserTask
from app.helper import user_tasks, save_tasks
from app.utils import create_response

router = APIRouter()

@router.get("/tasks")
def get_all_tasks():
    if not user_tasks or all(len(tasks) == 0 for tasks in user_tasks.values()):
        return create_response(True, "No tasks added yet", {"tasks": {}})

    return create_response(True, "All user tasks", {"tasks": user_tasks})

@router.get("/tasks/{username}")
def get_user_tasks(username: str):
    tasks = user_tasks.get(username)
    if tasks is None:
        raise HTTPException(status_code=404, detail="User not found")
    return create_response(True, f"Tasks for {username}", {"tasks": tasks})

@router.post("/tasks", status_code=201)
def create_task(user_task: UserTask):
    user = user_task.user_name
    task = user_task.task.model_dump()

    user_tasks.setdefault(user, [])

    if any(t["task_name"] == task["task_name"] for t in user_tasks[user]):
        raise HTTPException(status_code=409, detail="Task already exists for this user")

    user_tasks[user].append(task)
    save_tasks()
    return create_response(True, "Task added", {"tasks": user_tasks[user]})

@router.put("/tasks/{username}/{task_name}")
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

@router.delete("/tasks/{username}/{task_name}")
def delete_task(username: str, task_name: str):
    tasks = user_tasks.get(username)
    if not tasks:
        raise HTTPException(status_code=404, detail="User not found")

    new_tasks = [task for task in tasks if task["task_name"] != task_name]

    if len(new_tasks) == len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")

    user_tasks[username] = new_tasks
    save_tasks()
    return create_response(True, "Task deleted", {"remaining_tasks": new_tasks})
