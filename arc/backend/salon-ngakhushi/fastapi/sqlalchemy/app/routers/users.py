from fastapi import APIRouter, FastAPI, Depends
from ..schemas import User, Updateuser
from ..dependencies import db_dependency
import models

router= APIRouter(    
    tags= ["users"],
    responses= {404: {"description": "Not found"}}
)

@router.get("/users") 
async def get_users(db: db_dependency): #type:ignore
    return db.query(models.User).all()

@router.post("/create-user")
async def add_user(user: User, db: db_dependency): #type:ignore
    new_user= models.Users(user_id= user.user_id, name= user.name, team= user.team, latest_task= user.latest_task)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "New User Added!\n{new_user}"}

@router.put("/edit-user")
async def update_user(user: Updateuser, db: db_dependency): #type:ignore
    new_user= models.Users(user_id= user.user_id, name= user.name, team= user.team, latest_task= user.latest_task)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "New User Added!\n{new_user}"}