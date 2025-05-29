class Person:
    def init(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def greet(self):
        return f"My name is {self.fname} {self.lname} and I am {self.age} years old."
    
class User(Person):
    def init(self, fname, lname, age, username, tasks):
        super().init(fname, lname, age)
        self.username = username
        self.tasks = tasks

    def display(self):
        return f"Username: {self.username}, Tasks: {self.tasks}"

user1= User('Hiro', 'Roku', 21, 'hro32', '3 out of 4')
print(user1.display)