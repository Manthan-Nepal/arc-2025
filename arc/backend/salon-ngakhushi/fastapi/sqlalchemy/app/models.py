from sqlalchemy import Column, ForeignKey, DateTime, String, Integer, func, BigInteger
from app.dbconnection import Base

class Tasks(Base):
    __tablename__= "tasks"
    day= Column(Integer, primary_key= True, unique= True, nullable= False)
    title= Column(String, unique= True, nullable= False)
    description= Column(String, nullable= False)
    team= Column(String(10))

class Dailytasks(Base):
    __tablename__="daily_tasks"
    task_no= Column(Integer, primary_key= True, nullable= False)
    task= Column(String, nullable= False, unique= True)
    day= Column(Integer, ForeignKey("tasks.day"), index= True, nullable= False)
    
class Users(Base):
    __tablename__= "users"
    user_id= Column(BigInteger, primary_key= True, unique= True, nullable= False)
    name= Column(String, unique= True, nullable= False)
    hashed_password= Column(String)
    team= Column(String, nullable= False)
    latest_task= Column(Integer, ForeignKey("daily_tasks.task_no"), index= True, nullable= False)

class Taskstatus(Base):
    __tablename__= "task_status"
    log_id= Column(BigInteger, primary_key= True, nullable= False)
    user_id= Column(Integer, ForeignKey("users.user_id"), index= True, nullable= False)
    task_no= Column(Integer, ForeignKey("daily_tasks.task_no"), index= True, nullable= False)
    status= Column(String, nullable= False)

