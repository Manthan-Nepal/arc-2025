from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()


db= [{"name": "Hiro"}, {"name": "Siro"}, {"name": "Yura"}, {"name": "Yuji"}, {"name": "Bora"}, {"name": "Hima"}]

class User:
    def __init__(self, message: str| None=None, skip: int= 0, limit: int= 10):
        self.message= message
        self.skip= skip
        self.limit= limit
        
@app.get("/users/")
async def get_db(user: User= Depends()):
    response= {}
    if user.message:
        response.update({"Message": user.message})
        
    users= db[user.skip: 3]
    
    response.update({"users": users})    
    return response