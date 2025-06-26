from pydantic import BaseModel # type: ignore
from typing import Optional, Literal

class Tasks(BaseModel):
    day: int
    title: str
    description: str
    
class Updatetask(BaseModel):
    day: Optional[str]= None
    title: Optional[str]= None
    description: Optional[str]= None

class Taskstatus(BaseModel):
    log_id:int
    user_id: int
    status: Literal["todo", "inprogress", "completed"]
    day: int
    
class User(BaseModel):
    user_id: int
    name: str
    team: Literal["AI", "Frontend", "Backend", "UI/UX"]
    latest_task: int