from functools import reduce

# Reduce: reduces elements from a collection to a single value,
# good for funtional usage
# Syntax: reduce(funtion, collection)

marks= [56, 89, 72, 63, 90]
print("Marks: ", marks)
def sum(x, y):
    return x+y

total= reduce(sum, marks)
print("\nTotal Marks using function: ", total)

total2= reduce(lambda a, b: a+b,  marks)
print("\nTotal Marks with Lambda: ", total2)

# Filter: returns all elemets that match a condition
# Syntax: filter(funtion, collection)

def distinct(marks):
    return marks>=80

filtered1= list(filter(distinct, marks))
print("\nDistinction from function: ", filtered1)

filtered2= list(filter(lambda a: a>=80, marks))
print("\nDistinction from Lambda: ", filtered2)

