from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/long-task")
async def long_running_task():
    await asyncio.sleep(5)  
    return {"message": "Task completed after 5 seconds"}
