# Write a function that uses *args and **kwargs to print all passed values in formatted string example: Hello : name: "hari", roll:2, something like this.

# def use(*name):
#     for i in (name):
#         print(f"{i}")

def args(*args):
    # for val, value in enumerate(args):
    #     print(value)
    a,b,c = args
    print(a)

def kwargs (**kwargs):
    for key, val in kwargs.items():
        print(f" {key}: {val}")

kwargs(name = "hari", roll = 2)
args(10,20,30)