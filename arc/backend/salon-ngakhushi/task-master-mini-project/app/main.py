from fastapi import FastAPI, Path, APIRouter
from app.schemas import Tasks, Updatetask
from .routers import user, tasks
from .internal import admin

app= FastAPI() 
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

