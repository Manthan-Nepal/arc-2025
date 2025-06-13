from fastapi import FastAPI, Path, APIRouter
from app.schemas import Task, Updatetask
from .routers import user, tasks
from .internal import admin

app= FastAPI() #uvicorn app_name:app --reload fastapi dev main.py
app.include_router(tasks.router)
app.include_router(user.router)
app.include_router(
    admin.router,
    prefix= "/admin",
    tags= ["admin"],
    dependencies= [],
    responses= {418: {"description": "No Admin?"}}
)

@app.get("/")
def root():
    return {"message": "This is the root path."}

