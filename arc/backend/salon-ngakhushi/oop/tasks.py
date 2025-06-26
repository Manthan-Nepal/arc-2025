from abc import abstractmethod
class Task:
    def __init__(self, title, description, status):
        self.title= title
        self.description= description
        self.status= status
        
    def Ttitle(self):
        print(f"The title of this task is: {self.title}.")
        
    def Tdesc(self):
        print(f"This task is about: {self.description}.")
    
    @abstractmethod    
    def Tstatus(self):
        pass

class User(Task):
    def __init__(self, username, title, description, status):
        super().__init__(title, description, status)
        self.username= username
    
    def Tstatus(self):    
        if self.status=='completed':
            print(f"{self.username} has completed Task: {self.title}.")
        
        elif self.status=='incomplete':
            print(f"{self.username} has yet to complete Task: {self.title}.")
            
        elif self.status=='received':
            print(f"{self.username} has receive a new Task: {self.title}.")
        else:
            print("Task status not submitted.")
        

user1= User('Salon Ngakhushi', 'Python Basics', 'Python Syntax, Variables, Programming Concepts, Git and Github', 'completed')
task1= Task('Python Basics', 'Python Syntax, Variables, Programming Concepts, Git and Github', 'received')

print()
task1.Ttitle()
task1.Tdesc()
task1.Tstatus()
user1.Tstatus()
print()