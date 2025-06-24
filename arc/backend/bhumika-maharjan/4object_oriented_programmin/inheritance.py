class Person:
    def socialize(self):
        print("interavtive socializing")

class User(Person):
    # def socialize(self):  
    #     print("quiet socializing")
    def introduce(self):
        print("introvert")

user1 = User()
user1.socialize()
user1.introduce()