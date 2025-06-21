import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from .routers import users, tasks
from app.dbconnection import engine, Base

app= FastAPI()
app.include_router(tasks.router)
app.include_router(users.router)
       
Base.metadata.create_all(bind=engine)

