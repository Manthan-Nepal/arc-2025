from sqlalchemy.orm import Session
from . import models

def create_user(db: Session, name: str, email: str):
    user = models.User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_task(db: Session, title: str, description: str, owner_id: int):
    task = models.Task(title=title, description=description, owner_id=owner_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task


def get_user_tasks(db: Session, user_id: int):
    return db.query(models.Task).filter(models.Task.owner_id == user_id).all()


def search_tasks(db: Session, query: str):
    return db.query(models.Task).filter(
        models.Task.search_vector.match(query, postgresql_regconfig='english')
    ).all()
