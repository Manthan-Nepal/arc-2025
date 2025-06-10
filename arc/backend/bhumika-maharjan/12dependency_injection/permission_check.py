from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    role: str  

def get_current_user() -> User:
    return User(username="john", role="user")  

def require_admin(user: User = Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to access this resource"
        )
    return user

@app.get("/admin")
def read_admin_data(user: User = Depends(require_admin)):
    return {"message": f"Welcome, {user.username}. You have admin access."}
