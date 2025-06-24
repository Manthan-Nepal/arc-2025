from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Any

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item


@app.get("/items/", response_model=list[Item])
async def read_items() -> Any:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None

# @app.post("/user/")
# async def create_user(user: UserIn) -> UserIn:
#     return user

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIns(BaseUser):
    password: str


@app.post("/users/")
async def create_user(user: UserIn) -> BaseUser:
    return user