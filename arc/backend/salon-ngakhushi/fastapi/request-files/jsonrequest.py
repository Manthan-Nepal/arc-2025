from typing import List
from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel # type: ignore
import json

app = FastAPI()

class DataConfiguration(BaseModel):
    textColumnNames: List[str]
    idColumn: str

@app.post("/data")
async def data(
    dataConfiguration: str = Form(...),  
    csvFile: UploadFile = File(...)
):    
    data_config = DataConfiguration(**json.loads(dataConfiguration))
    content = await csvFile.read()
    print(f"Received file: {csvFile.filename}, content: {content}")
    print(f"Received data: {data_config}")
    return {"filename": csvFile.filename, "data": data_config}