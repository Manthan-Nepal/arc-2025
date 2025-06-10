from fastapi import FastAPI, status
from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional

app = FastAPI()


class Tasks(BaseModel):
    task_id: int = Field(..., ge=1, lt=10000)
    task_name: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., max_length=200)

class User(BaseModel):
    # user_id: int = Field(..., gt=0)
    user_id: int
    user_name: str = Field(..., min_length=2, max_length=30)
    email: EmailStr

    @field_validator("user_id")
    @classmethod
    def validate_user_id(cls, value):
        if value <= 0:
            raise ValueError("user_id must be a positive integer greater than 0")
        return value
    
    


class TaskCreate(BaseModel):
    task_name: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., max_length=200)

class TaskUpdate(BaseModel):
    task_name: Optional[str] = Field(None, min_length=3, max_length=50)
    description: Optional[str] = Field(None, max_length=200)



#Response models    

class AssignTaskResponse(BaseModel):
    message: str
    task: Tasks
    user: User

class TaskOut(BaseModel):
    task_id: int
    task_name: str
    description: Optional[str]

class TaskUpdateResponse(BaseModel):
    task_id: int
    task_name: Optional[str] = None
    description: Optional[str] = None


@app.post("/assigntasks", response_model=AssignTaskResponse)
async def assign_task(
    task: Tasks,
    user: User
):
    return {
        "message": "Task assigned successfully",
        "task": task,
        "user": user
    }


@app.post("/tasks/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskCreate):
    instant_task_id = 1  
    return {
        "task_id": instant_task_id,
        "task_name": task.task_name,
        "description": task.description
    }


@app.put("/tasks/{task_id}", response_model=TaskUpdateResponse)
async def update_task(task_id: int, task: TaskUpdate):
    return {
        "task_id": task_id,
        **task.model_dump(exclude_unset=True)
    }
