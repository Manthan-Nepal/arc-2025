from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.exc import SQLAlchemyError

DATABASE_URL = "postgresql://postgres:postgrespassword@localhost/fastapi"

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    tasks = relationship("Task", back_populates="owner")


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="tasks")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)

def assign_task_atomically(user_name: str, task_title: str, task_description: str):
    session = SessionLocal()
    try:
        
        with session.begin():            
            user = User(name=user_name)
            session.add(user)
            session.flush() 

            task = Task(title=task_title, description=task_description, owner_id=user.id)
            session.add(task)

        print("Task assigned atomically.")
    except SQLAlchemyError as e:
        session.rollback()
        print("Failed to assign task atomically:", str(e))
    finally:
        session.close()


if __name__ == "__main__":
    assign_task_atomically(
        user_name="Alice",
        task_title="Prepare report",
        task_description="Prepare report"
    )
