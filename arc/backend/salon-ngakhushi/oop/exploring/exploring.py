class Task:
    # Attributes are the variables inside a class
    def __init__(self, type, topic, status, remarks): 
        self.type= type
        self.topic= topic
        self.status= status
        self.remarks= remarks
    
    # Methods are functions inside a class    
    def progress(self):
        print(f"Task {self.topic} is {self.status}")
        
task1= Task("Self Learn", "Python OOP", "in progress", "interesting")
print(task1.topic)

task2= Task("Hands on", "OOP Class", "in progress", "understanding")
print(task2.remarks)

task2.progress()