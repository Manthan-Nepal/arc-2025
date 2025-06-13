from fastapi import FastAPI, Depends, HTTPException, Header
from typing import Annotated
from fastapi.security import APIKeyHeader

app= FastAPI()

API_KEY= "individualapikey"
API_KEY_NAME= "TEST-API-KEY"
API_KEY_HEADER= APIKeyHeader(name= API_KEY_NAME, auto_error= False)

def get_api_key(api_key: str= Depends(API_KEY_HEADER)):
    if api_key == API_KEY:
        return api_key
    else:
        raise HTTPException(status_code= 403, detail="Invalid API key.")

@app.get("/login")
def protected_route(api_key: str= Depends(get_api_key)):
    return {"message": "Access granted", "api_key": api_key}

@app.get("/view")
def public_route():
    return {"message": "This is the view route."}