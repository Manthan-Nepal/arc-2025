from fastapi import FastAPI


app = FastAPI()

task_list = [
    {"taskid": 1, "name": "abc", "status": "done"},
    {"taskid": 2, "name": "write report", "status": "in progress"},
    {"taskid": 3, "name": "email client", "status": "pending"},
    
]


@app.get("/tasks/")
async def get_tasks(status: str | None = None):
    if status:
        result = [task for task in task_list if task["status"] == status]
        return result
    return task_list
    