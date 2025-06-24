
from fastapi import FastAPI
from task.database import Base, engine
from task import auth, crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(crud.router)
