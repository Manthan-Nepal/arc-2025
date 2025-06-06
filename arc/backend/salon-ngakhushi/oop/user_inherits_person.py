from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    @abstractmethod
    def greet(self):
        pass
    
class User(Person):
    def __init__(self, fname, lname, age, username, tasks):
        super().__init__(fname, lname, age)
        self._username = username
        self.tasks = tasks

    
    def greet(self):
        return print(f"\nMy name is {self.fname} {self.lname} and I am {self.age} years old.")
    
    @property
    def display(self):
        return print(f"\nUsername: {self._username}, Tasks: {self.tasks}", end="\n\n")

user1= User(fname='Hiro', lname='Roku', age=21, username='hro32', tasks='3 out of 4')

user1.greet()
# user1.display()
print(user1._username)