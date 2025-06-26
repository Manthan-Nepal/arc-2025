from app.dbconnection import SessionLocal
from sqlalchemy.orm import Session # type: ignore
from typing import Annotated
from fastapi import Depends

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency= Annotated[Session, Depends(get_db)]