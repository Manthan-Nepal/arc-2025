from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    created_at: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

@app.get("/item", response_model=Item)
def get_item():
    return Item(id=1, name="Test Item", created_at=datetime.now())
