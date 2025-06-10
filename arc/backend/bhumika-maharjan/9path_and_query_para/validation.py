from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/search/")
async def search_items(
    q: str = Query(..., min_length=3, max_length=50, regex="^[a-zA-Z ]+$")
):
    return {"query": q}