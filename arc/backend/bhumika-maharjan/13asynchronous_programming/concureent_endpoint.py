from fastapi import FastAPI
import asyncio

app = FastAPI()

async def fetch_data(item_id: int):
    await asyncio.sleep(2) 
    return {"item_id": item_id, "data": f"Data for item {item_id}"}

@app.get("/concurrent-requests")
async def concurrent_requests():
    tasks = [fetch_data(i) for i in range(1, 6)]
    results = await asyncio.gather(*tasks)
    return {"results": results}
