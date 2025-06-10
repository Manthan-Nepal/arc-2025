import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE) or os.stat(TASKS_FILE).st_size==0:
        return []
    with open(TASKS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append({'task': task})
    save_tasks(tasks)
    print(f"Task added: {task}")



if __name__ == "__main__":
    add_task("Buy groceries")
    add_task("Finish project")

