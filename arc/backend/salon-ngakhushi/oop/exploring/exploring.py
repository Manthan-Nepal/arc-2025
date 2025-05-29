class task:
    def __init__(self, type, topic, status, remarks):
        self.type= type
        self.topic= topic
        self.status= status
        self.remarks= remarks
        
task1= task("Self Learn", "Python OOP", "in progress", "interesting")
print(task1.topic)

task2= task("Hands on", "OOP Class", "in progress", "understanding")
print(task2.remarks)