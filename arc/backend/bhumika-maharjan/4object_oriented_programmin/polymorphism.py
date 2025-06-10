#duck typing
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def make_it_talk(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

make_it_talk(dog) 
make_it_talk(cat)



#operator overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1 + p2  

print(p3) 




#method overiding
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self): 
        print("Woof! Woof!")

class Cat(Animal):
    def speak(self):  
        print("Meow!")


animal = Animal()
dog = Dog()
cat = Cat()

animal.speak()  
dog.speak()     
cat.speak()    

