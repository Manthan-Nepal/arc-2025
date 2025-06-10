class Task:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"{self.title} - {self.description} Status - [{self.status}]"
    
class PriorityTask(Task):
    def __init__(self, title, description, status, priority):
        super().__init__(title, description, status)
        self.priority = priority

    def __str__(self):
        return f"{self.title} - {self.description} Status - [{self.status}] Priority = {self.priority}"
    
class User:
    def __init__(self):
        self.tasks=[]

    def add_task(self, title, description, status):
        task=Task(title, description, status)
        self.tasks.append(task)
        return self.tasks
    
    def add_priority_task(self, title, description, status, priority):
        task = PriorityTask(title, description, status, priority)
        self.tasks.append(task)
        return self.tasks 
    
    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Task removed.")
                return
        print(f"Task not found ")

    def list_tasks(self):
        if not self.tasks:
            print(f"No tasks found.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")



baker = User() 
baker.add_task("Bake Cookies", "Prepare and bake chocolate chip cookies", "pending")
baker.add_priority_task("Make Dough", "Mix flour, sugar, and eggs", "To do", "High")
baker.list_tasks()

