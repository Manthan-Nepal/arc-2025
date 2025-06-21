from pydantic import BaseModel # type: ignore
from typing import Optional, Literal, List

class Tasks(BaseModel):
    day: int
    title: str
    description: str
    daily_tasks: List[int]

class Dailytasks(BaseModel):
    day: int 
    task_no: int
    task: str      

class Updatetask(BaseModel):
    day: Optional[str]= None
    title: Optional[str]= None
    description: Optional[str]= None

class Taskstatus(BaseModel):
    log_id: Optional[int]= None
    user_id: int
    status: Literal["todo", "inprogress", "completed"]
    day: int
    
class Updatetaskstatus(BaseModel):
    log_id: Optional[int]= None
    user_id: Optional[int]= None
    status: Optional[Literal["todo", "inprogress", "completed"]]= None
    day: Optional[int]= None
    
class User(BaseModel):
    user_id: int
    name: str
    team: Literal["AI", "Frontend", "Backend", "UI/UX"]
    latest_task: int
    
class Updateuser(BaseModel):
    user_id: Optional[int]= None
    name: Optional[str]= None
    team: Optional[Literal["AI", "Frontend", "Backend", "UI/UX"]]= None
    latest_task: Optional[int]= None
    
