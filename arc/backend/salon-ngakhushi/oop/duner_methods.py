class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"

    def __repr__(self):
        return f"Person: {self.name!r}" 'hkd'

    def __eq__(self, other):
        # if isinstance(other, Person):
        return self.name == other.name
        # return False

p1 = Person("Hiro")
p2 = Person("Yura")

print(str(p1))
print(repr(p2))
print(p1==p2) 