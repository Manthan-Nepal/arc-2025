from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File()]):
#     return {"file_size": len(file)}

@app.post("/files/")
async def create_files(files: Annotated[list[bytes], File()]):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.content_type}

# @app.post("/uploadfiles/")
# async def create_upload_files(files: list[UploadFile]):
#     return {"filenames": [file.filename for file in files]}

@app.post("/read-file/")
async def read_file(file: UploadFile = File(...)):
    content = await file.read() 
    text = content.decode("utf-8")  
    return {"content": text}
