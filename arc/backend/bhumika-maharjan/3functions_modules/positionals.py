def greet_user(name, greeting="Hello", punctuation="!"):
    print(f"{greeting}, {name}{punctuation}")


greet_user("World")
greet_user("John", greeting="Hi")  
greet_user("Sir", punctuation=".") 

def print_numbers(*args):
    for num in args:
        print(num)

print_numbers(1, 2, 3, 4)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="naam", age=20, country="Nepal")
