class animal:
    def __init__(self, name):
        self.name= name
    
    def likes(self):
        print(f"{self.name} like Food.")
        
    def sleeps(self):
        print(f"{self.name} sleeps alot.")
        
class dog(animal):
    pass

class cat(animal):
    pass

dog1= dog("Ben")
dog2= dog("Yoru")
cat1= cat("Siro")
cat2= cat("Hen")

print(dog1.name)