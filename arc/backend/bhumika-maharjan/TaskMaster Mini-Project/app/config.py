from dotenv import load_dotenv
import os

load_dotenv()

TASKS_FILE = os.getenv("TASKS_FILE", "data/tasks.json")  
