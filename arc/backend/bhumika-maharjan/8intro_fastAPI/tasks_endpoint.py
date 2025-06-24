from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    task_name: str
    status: Union[str, None] = None

@app.get("/")
def read_root():
    return "GO TO /tasks"

mock_tasks = [
    Task(task_name="abc", status="pending"),
    Task(task_name="xyz", status="completed")
]

@app.get("/tasks")
def get_tasks():
    return mock_tasks

@app.get("/tasks/{task_id}")
def load_tasks(task_id: int, q:Union[str, None]=None):
    return {"task_id": task_id, "q":q}

@app.put("/tasks/{task_id}")
def update_tasks(task_id: int, task:Task):
    return {"task_id": task_id, "task_name": task.task_name, "task_status": task.status}
