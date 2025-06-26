from fastapi import FastAPI, File, UploadFile, HTTPException # type:ignore
from typing import Annotated
from fastapi.responses import HTMLResponse, FileResponse # type: ignore
import os

app= FastAPI()

ALLOWED_MIME_TYPES= ["image/png", "application/pdf"]
uploaded_files= "files"

# File() stores file data in memory as bytes
@app.post("/files/")
async def create_file(file: Annotated[bytes, File(description= "Reading bytes")]):
    return {"file_size": len(file)}

# UploadFile will store file to drive if a limit is reached
@app.post("/uploadfiles")
async def upload_files(files: list[UploadFile]):
    print("hello")
    if not files:
        return {"message": "No file uploaded."}
    else:
        return {"filenames": [file.filename for file in files]}

@app.get("/files/{filename}")
async def download_file(filename):
    file_path= os.path.join(uploaded_files, filename)
    if not os.path.isfile(file_path):
        return {"Error": "File not found"}
    return FileResponse(path= file_path, filename= filename)
    
   
@app.post("/uploadfile/")
async def upload_files(file: UploadFile):
    if not file:
        return {"message": "No file uploaded."}
    else:
        if file.content_type not in ALLOWED_MIME_TYPES:
            raise HTTPException(status_code= 400, detail= "File type must be PNG or PDF.")
        return {"filename": file.filename}

@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

    

    



