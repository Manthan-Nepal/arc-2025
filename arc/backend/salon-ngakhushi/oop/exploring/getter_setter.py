class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class User(Person):
    def __init__(self, name, age, username, email):
        super().__init__(name, age)
        self.username = username
        self._email = email  

    # Getter
    @property
    def email(self):
        return self._email

    # Setter
    @email.setter
    def email(self, updatedmail):
        if "@" not in self.email:
            self._email= updatedmail
        else:
            print("Email is valid.")
        

    
user = User("Hiro", 30, "hiro32", "hiro@gmail.com")
print(user._email)

user2= User("Yura", 12, "yureru", "yura@gmail.com")
print(user2.email)
