from pydantic import BaseModel # type: ignore
from typing import Optional, Literal

class Task(BaseModel):
    day: str
    title: str
    status: Literal["Completed", "Incomplete"]
    
class Updatetask(BaseModel):
    day: Optional[str]= None
    title: Optional[str]= None
    status: Optional[str]= None
    
class User(Task):
    name: str
    team: Literal["AI", "Frontend", "Backend", "UI/UX"]
    tasks: Task