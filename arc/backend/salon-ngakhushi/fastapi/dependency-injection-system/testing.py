from fastapi import Depends, FastAPI, Cookie
from typing import Annotated

app = FastAPI()


async def common_parameters(name: str | None = None, skip: int = 0, limit: int = 100):
    return {"name": name, "skip": skip, "limit": limit}

common_dependency= Annotated[dict, Depends(common_parameters)]

@app.get("/items/")
async def read_items(commons: common_dependency):
    return commons


@app.get("/users/")
async def read_users(commons: common_dependency):
    return {"hi"}


@app.get("/items/")
async def read_items(cookie: Annotated[str | None, Cookie()] = None):
    return {"cookie": cookie}