from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

app = FastAPI()



class ErrorResponse(BaseModel):
    detail: str
    code: int
    message: str

@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    return JSONResponse(
        status_code=HTTP_404_NOT_FOUND,
        content={
            "detail": "Resource not found",
            "code": 404,
            "message": "The requested item does not exist."
        }
    )

@app.exception_handler(500)
async def internal_error_handler(request: Request, exc):
    return JSONResponse(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "detail": "Internal Server Error",
            "code": 500,
            "message": "An unexpected error occurred."
        }
    )


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id != 1:
        raise HTTPException(status_code=404)
    return {"item_id": item_id, "name": "Sample Item"}

@app.get("/error")
async def error():
    1 / 0
    return {"message": "This won't be reached"}