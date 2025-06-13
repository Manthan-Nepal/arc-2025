from fastapi import APIRouter, FastAPI, Depends
from ..schemas import User

router= APIRouter(    
    tags= ["users"],
    dependencies= [Depends(User)],
    responses= {404: {"description": "Not found"}}
)

@router.get("/users",)
async def read_users():
    return [{"username": User.name}]

@router.get("/user-tasks/")
async def read_user_tasks():
    return [{"User Tasks": User.tasks}]