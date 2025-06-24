import json
import os
from typing import Dict, List
from app.config import TASKS_FILE

user_tasks: Dict[str, List[Dict[str, str]]] = {}

def load_tasks():
    global user_tasks
    if not os.path.exists(TASKS_FILE):
        user_tasks = {}
    else:
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            user_tasks = json.load(f)

def save_tasks():
    os.makedirs(os.path.dirname(TASKS_FILE), exist_ok=True)
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(user_tasks, f, indent=4)


load_tasks()
