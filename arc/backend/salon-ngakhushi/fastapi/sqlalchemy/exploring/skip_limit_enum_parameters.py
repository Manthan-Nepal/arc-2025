from fastapi import FastAPI
from typing import Optional
from enum import Enum

app= FastAPI()

class Enumtest(str, Enum):
    enum1= "Enum1"
    enum2= "Enum2"
    enum3= "Enum3"

someitems= [2, 54, 1, 19, 2, 99]

#needy is a required str
# skip is the starting point,default value 0
# limit is the limited number of elements, int
  
@app.get("/items")
def items(skip: int= 1, limit: int= 4):
    return print(someitems[skip: skip+limit])
items()

@app.get("/enumx/{enumnum}")
def enumx(enumnum: Enumtest):
    if enumnum is Enumtest.enum1:
        return {"enum_num": enumnum, "message": "Hehehaha"}
    
    if enumnum is Enumtest.enum2:
        return {"enum_num": enumnum, "message": "Hehahaha"}
    
    if enumnum is Enumtest.enum3:
        return {"enum_num": enumnum, "message": "Hahahaha"}
