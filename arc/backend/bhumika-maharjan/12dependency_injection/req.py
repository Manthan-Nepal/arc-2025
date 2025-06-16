from fastapi import FastAPI, Header, Query, Path, UploadFile, File, Depends, HTTPException

app = FastAPI()

def get_name(name: str = Header(...)):
    if not name.strip():
        raise HTTPException(status_code=400, detail="Name cannot be empty")
    return name

@app.get("/greet-header")
async def greet(name: str = Depends(get_name)):
    return {"message": f"Hello, {name}!"}


@app.get("/greet-query")
async def greet(name: str = Query(...)):
    return {"message": f"Hello, {name}!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(...)):
    return {"item_id": item_id}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    return {"filename": file.filename}

