from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional

app = FastAPI()


class Tasks(BaseModel):
    task_id: int = Field(..., ge=1, lt=10000)
    task_id: int 
    task_name: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., max_length=200)

class User(BaseModel):
    # user_id: int = Field(..., gt=0)
    user_name: str = Field(..., min_length=2, max_length=30)
    email: EmailStr

    

@app.post("/assigntasks")
async def assign_task(
    task: Tasks,
    user: User
):
    return {
        "message": "Task assigned successfully",
        "task": task,
        "user": user
    }


class TaskCreate(BaseModel):
    task_name: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., max_length=200)

class TaskUpdate(BaseModel):
    task_name: Optional[str] = Field(None, min_length=3, max_length=50)
    description: Optional[str] = Field(None, max_length=200)



@app.post("/tasks/")
async def create_task(task: TaskCreate):
    return task

@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: TaskUpdate):
    return {"task_id": task_id, **task.model_dump(exclude_unset=True)}