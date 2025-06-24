from fastapi import Depends, FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str

fake_db = [
    Item(id=1, name="Item One"),
    Item(id=2, name="Item Two"),
]


async def get_db():
    try:
        yield fake_db
    finally:
        pass  

@app.get("/items/", response_model=List[Item])
async def read_items(db=Depends(get_db)):
    return db
