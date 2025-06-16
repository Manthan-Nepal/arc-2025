from fastapi import APIRouter, HTTPException
from app.helper import user_tasks, save_tasks
from app.utils import create_response

router = APIRouter()

@router.get("/users")
def list_users():
    users = list(user_tasks.keys())
    if not users:
        return create_response(True, "No users added yet", {"users": []})
    return create_response(True, "Users retrieved successfully", {"users": users})

@router.delete("/users/{username}")
def delete_user(username: str):
    if username not in user_tasks:
        raise HTTPException(status_code=404, detail="User not found")

    del user_tasks[username]
    save_tasks()
    
    return create_response(True, f"User '{username}' and all their tasks deleted", {"remaining_users": list(user_tasks.keys())})
