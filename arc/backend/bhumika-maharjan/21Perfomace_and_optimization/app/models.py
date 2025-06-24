from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date, Index
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.dialects.postgresql import TSVECTOR

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)

    tasks = relationship("Task", back_populates="owner", cascade="all, delete-orphan")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=True)
    description = Column(Text, nullable=True)
    due_date = Column(Date, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    search_vector = Column(TSVECTOR)
    owner = relationship("User", back_populates="tasks")

    __table_args__ = (
        Index("ix_tasks_search_vector", "search_vector", postgresql_using="gin"),
    )

