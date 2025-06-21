from sqlalchemy import Column, ForeignKey, DateTime, String, Integer, func, BigInteger
from app.dbconnection import Base

class Tasks(Base):
    __tablename__= "tasks"
    day= Column(Integer, primary_key= True, index= True, unique= True, nullable= False)
    title= Column(String, index= True, unique= True, nullable= False)
    description= Column(String, nullable= False)

class Dailytasks(Base):
    __tablename__="daily_tasks"
    task_no= Column(Integer, primary_key= True, index= True, nullable= False)
    task= Column(String, nullable= False, index= True, unique= True)
    day= Column(Integer, ForeignKey("tasks.day"), index= True, nullable= False)
    
class Users(Base):
    __tablename__= "users"
    user_id= Column(BigInteger, primary_key= True, index= True, unique= True, nullable= False)
    name= Column(String, index= True, unique= True, nullable= False)
    team= Column(String, nullable= False)
    latest_task= Column(Integer, ForeignKey("daily_tasks.task_no"),  index= True, nullable= False)

class Taskstatus(Base):
    __tablename__= "task_status"
    log_id= Column(BigInteger, primary_key= True, index= True, nullable= False)
    user_id= Column(Integer, ForeignKey("users.user_id"), index= True, nullable= False)
    task_no= Column(Integer, ForeignKey("daily_tasks.task_no"), index= True, nullable= False)
    status= Column(String, index= True, nullable= False)
    
    
class Company(Base):
    __tablename__= 'company'    
    id= Column(BigInteger, primary_key= True, nullable= False)
    name= Column(String(30), unique= True, nullable= False)
    address= Column(String(20), nullable= False)
    created_at= Column(DateTime, default= func.now())
