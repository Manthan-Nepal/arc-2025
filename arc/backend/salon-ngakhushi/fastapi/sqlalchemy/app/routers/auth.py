from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime, timedelta
from sqlalchemy.orm import Session  #type:ignore
from jose import jwt, JWTError   #type:ignore
from passlib.context import CryptContext    #type:ignore
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer    #type:ignore
from starlette import status    #type:ignore
from typing import Annotated
from pydantic import BaseModel  #type: ignore

from ..dependencies import db_dependency
from ..dbconnection import SessionLocal
from ..schemas import Users
import models

router= APIRouter(
    prefix= '/auth',    
    tags= ["auth"],
    responses= {404: {"description": "Not found"}}
)

ALG= 'HS256'
SECRET_KEY= 'secretkey123456789'

bcrypt_context= CryptContext(schemes= ['bcrypt'], deprecated= 'auto')
oauth2_bearer= OAuth2PasswordBearer(tokenUrl = 'auth/token')

class CreateUserRequest(Users):
    pass

class Token(BaseModel):
    access_token: str
    token_type: str

@router.get("/")
async def root():
    return {"This is the root auth path"}

@router.post("/", status_code= status.HTTP_201_CREATED)
async def create_user(create_user_request: CreateUserRequest, db: db_dependency):
    new_user= models.Users(
        name= create_user_request.name,
        hashed_password= bcrypt_context.hash(create_user_request.hashed_password),
        team= create_user_request.team,
        latest_task= create_user_request.latest_task
    )
    print(new_user)
    db.add(new_user)
    db.commit()
    return {"message": "New User created successfully"}

@router.post("/token", response_model= Token)
async def login_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], 
                             db: db_dependency):
    user= authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,
                            detail= "User could not be validated.")
    token= create_token(user.name, user.user_id, timedelta(minutes=30))
    
    return {"access_token": token, "token_type": 'bearer'}    

def authenticate_user(username: str, password: str, db):
        user= db.query(models.Users).filter(models.Users.name == username).first()
        if not user:
            return False
        if not bcrypt_context.verify(password, user.hashed_password):
            return False
        return user
    
def create_token(username: str, user_id: int, expires_in: timedelta):
    encode= {'sub': username, 'id': user_id}
    expires= datetime.now() + expires_in
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm= ALG)

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload= jwt.decode(token, SECRET_KEY, algorithms= [ALG])
        username: str= payload.get('sub')
        user_id: int= payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,
                                detail= "User could not be validated.")
        return {'username': username, 'id': user_id}
    except JWTError:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,
                                detail= "User could not be validated.")