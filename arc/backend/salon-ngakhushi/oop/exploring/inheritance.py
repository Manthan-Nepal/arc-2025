class Animal:
    def __init__(self, name):
        self.name= name
    
    def likes(self):
        print(f"{self.name} likes Food.")
        
    def sleeps(self):
        print(f"{self.name} sleeps alot.")
        
class Dog(animal):
    def talk(self):
        print(f"{self.name} barks a lot.")
    
class Cat(animal):
    pass

class Poodle(dog):
    pass

dog1= Dog("Ben")
dog2= Dog("Yoru")
cat1= Cat("Siro")
cat2= Cat("Hen")
belly= Poodle("Belly")

print()
dog1.likes()
cat2.sleeps()
dog2.sleeps()
cat1.likes()
belly.talk()
print()