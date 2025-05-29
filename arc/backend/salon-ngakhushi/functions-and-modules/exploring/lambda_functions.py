# lambda makes a function inside a variable
# Takes any number of arguments but only has 1 expression
# useful for higher order functions
# syntax: lambda variable: expression

double= lambda a: a*2
print("\nDouble: ", double(3))

sum= lambda a, b: a+b
print("\nSum: ", sum(32, 13))

mini= lambda a, b: a if a<b else b
print("\nSmaller value is: ", mini(78, 4))

even= lambda a: a%2==0
print("Even or not in lambda: ", even(9))


# Map: performs a function action to a collection iteratively
# Syntax: map(function, collection)
# returns a map object unless specified, the map object iterates on the collection one at a time

temp= [32, 43, 56, 81, 29]
print("\n", temp)

def double(temp):
    return temp*2

two_multi= list(map(double, temp))[1:-1]
# two_multi= map(double, temp)
print("This is function in map", two_multi)

multiply_2= list(map(lambda a:a*2, temp))
print("This is lambda in map: ", multiply_2)

