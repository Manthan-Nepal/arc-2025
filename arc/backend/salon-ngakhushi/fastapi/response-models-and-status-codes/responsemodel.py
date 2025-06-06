from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any

app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: list[str] = []


# @app.post("/items/")
# async def create_item(item: Item) -> Item:
#     return item


# @app.get("/items/")
# async def read_items() -> list[Item]:
#     return [
#         Item(name="Apple", price= 20.0),
#         Item(name="Banana", price= 17.0),
#     ]
    
# @app.get("/items/", response_model=list[Item])
# async def read_items() -> Any:
#     return [
#         {"name": "Apple", "price": 20.0},
#         {"name": "Banana", "price": 17.0},
#     ]

app = FastAPI()


@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}