from fastapi import FastAPI, Depends, HTTPException, Header
from typing import Annotated

app= FastAPI()

async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str= Header(alias= "z-key")):
    if x_key != "key":
        raise HTTPException(status_code=400, detail="Z-Key header invalid")
    return x_key


@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]