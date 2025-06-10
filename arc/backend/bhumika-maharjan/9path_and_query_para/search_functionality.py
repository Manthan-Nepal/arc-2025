from fastapi import FastAPI, Query

items = [
    {"id": 1, "name": "apple"},
    {"id": 2, "name": "banana"},
    {"id": 3, "name": "cherry"},
    {"id": 4, "name": "date"},
]

app = FastAPI()

@app.get("/items/")
def search_item(q: str | None = None):
    if q:
        results = [item for item in items if q in item["name"]]
    else:
        results = items
    return {"results":results}
        