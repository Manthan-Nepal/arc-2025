from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import database, crud, models

app = FastAPI()

database.init_db()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    return crud.create_user(db, name=name, email=email)

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/tasks/")
def create_task(title: str, description: str, owner_id: int, db: Session = Depends(get_db)):
    return crud.create_task(db, title=title, description=description, owner_id=owner_id)

@app.get("/tasks/{task_id}")
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted"}


@app.get("/users/{user_id}/tasks")
def get_user_tasks(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_tasks(db, user_id)

@app.get("/tasks/search")
def search_tasks(q: str, db: Session = Depends(get_db)):
    results = crud.search_tasks(db, q)
    return results

