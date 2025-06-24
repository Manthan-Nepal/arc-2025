from pydantic import BaseModel

class Task(BaseModel):
    task_name: str
    status: str

class UserTask(BaseModel):
    user_name: str
    task: Task
