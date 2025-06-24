from task.database import SessionLocal
from sqlalchemy.orm import Session

def getdb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()