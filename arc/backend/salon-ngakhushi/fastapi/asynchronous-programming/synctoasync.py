from fastapi import FastAPI
import asyncio

app= FastAPI()

@app.get("/sync")
def syncfunc():
    return {"Synchronous Endpoint."}

@app.get("/async")
async def asyncfunc():
    await asyncio.sleep(3)
    return {"Asynchronous Endpoint."}