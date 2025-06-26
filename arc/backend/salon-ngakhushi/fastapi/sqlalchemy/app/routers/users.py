from fastapi import APIRouter, FastAPI, Depends, HTTPException
from ..schemas import Users, Updateuser
from ..dependencies import db_dependency
import models
from typing import Annotated
# from . import auth
from .auth import get_current_user

router= APIRouter(    
    tags= ["users"],
    responses= {404: {"description": "Not found"}}
)
user_dependency= Annotated[dict, Depends(get_current_user)]

@router.get("/user") 
async def get_user(user: user_dependency, db: db_dependency): #type:ignore
    if user is None:
        raise HTTPException(status_code= 401, detail= 'Authentication Failed')
    return {"User": user}

@router.put("/edit-user")
async def update_user(user: Updateuser, db: db_dependency): #type:ignore
    new_user= models.Users(user_id= user.user_id, name= user.name, team= user.team, latest_task= user.latest_task)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "New User Added!\n{new_user}"}