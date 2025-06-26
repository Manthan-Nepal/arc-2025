from sqlalchemy import Column, ForeignKey, Integer, String
from dbconnection import Base

class Tasks(Base):
    __tablename__= "tasks"
    
    day= Column("day", Integer, primary_key= True, index= True)
    title= Column(String, index= True)
    description= Column(String, index= True)

class Users(Base):
    __tablename__= "users"
    
    user_id= Column(Integer, primary_key= True, index= True)
    name= Column(String, index= True)
    team= Column(String, index= True)
    latest_task= Column(Integer, ForeignKey("tasks.day"),  index= True)

class Taskstatus(Base):
    __tablename__= "task_status"
    
    log_id= Column(Integer, primary_key= True, index= True)
    user_id= Column(Integer, ForeignKey("users.user_id"), index= True)
    day= Column(Integer, ForeignKey("tasks.day"), index= True)
    status= Column(String, index= True)