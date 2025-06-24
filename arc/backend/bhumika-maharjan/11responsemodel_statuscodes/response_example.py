from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    task_name: str
    status: str

@app.get(
    "/tasks/{task_name}",
    response_model=Task,
    responses={
        200: {
            "description": "Successful Response",
            "content": {
                "application/json": {
                    "example": {
                        "task_name": "Write docs",
                        "status": "completed"
                    }
                }
            },
        }
    }
)
def get_task(task_name: str):
    return {"task_name": task_name, "status": "completed"}
