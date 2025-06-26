from pydantic import BaseModel, EmailStr, PositiveInt, ValidationError, field_validator
from typing import Optional, Literal

class Task(BaseModel):
    day: str
    title: str
    # status: str
    status: Literal["Completed", "Incomplete"]
    
    # @field_validator('status')
    # async def status_validation(cls, value):
    #     if value != "Completed" or "Incomplete":
    #         raise ValueError("Invalid Task status.")
    #     return value         
    
class Updatetask(BaseModel):
    day: Optional[str]= None
    title: Optional[str]= None
    status: Optional[str]= None
    
class User(BaseModel):
    name: str
    team: Literal["AI", "Frontend", "Backend", "UI/UX"]