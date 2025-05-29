# any function returns true or false value, list can be used for multiple 'or' comparisions
print(any([False, False, False]))
print(any([False, True, False]))
print(any(['s'=='as', len('good')==4]))

# # Argument Precedentce: Positional->Keyword->Default->Arbritary(args, kwargs) 

# # Positional Parameter: can be empty
def parameter(one, uno, ichi):
    print(f"Two in english is {one}, spanish is {uno}, and japanese is {ichi}")


parameter('two', 'duo', 'ni')
#parameter() #Outputs error missing 3 positional argument
parameter('duo', 'ni', 'two')


# # Keyword Arguments: allows using arguments in any order if the keywords are specified 
parameter(uno='two', one='duo', ichi='ni')


def person(fname, phone, email):
    return print(f"\nMy name is {fname}, my phone number is {phone} and my email is {email}.")
person('Hiro', 7891038, email='hiro@gmail.com')


# # Default Argument
def person(fname, phone, email="person@gmail.com"):
    return print(f"\nMy name is {fname}, my phone number is {phone} and my email is {email}.")
person("Hiro", 7891038)


# # *args: Parameter name is variable, * is the defining part
def add(*numbers):
    sum=0
    for num in numbers:
        sum+=num
    return sum
print(add(2,3,4,5,6,7,8,9,1))

# The '*'(astresk) is called a packing function, kwargs uses two while args uses one '*'
# # **kwargs: short for Keyword Arguments, uses dictionary data structure
def person(**kwargs):
    print()
    for question, answer in kwargs.items():
        print(f"{question}: {answer}")
    print()
    for value in kwargs.values():
        print(f" {value}")

person(
    name='Hiro', 
    phone= 394237413, 
    email= 'hiro@gmail.com'
    )


