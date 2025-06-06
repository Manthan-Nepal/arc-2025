from pydantic import BaseModel, EmailStr, PositiveInt, ValidationError
from typing import Optional

class Task(BaseModel):
    day: str
    title: str
    status: str
    
class Updatetask(BaseModel):
    day: Optional[str]= None
    title: Optional[str]= None
    status: Optional[str]= None
    