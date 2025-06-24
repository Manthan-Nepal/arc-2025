from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from task import models, schemas
from task.dependecies import get_db
from task.auth import get_current_user

router = APIRouter()

@router.post("/login")
def loginuser(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}

@router.get("/users", response_model=List[schemas.UserOut])
def get_users(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.User).all()
