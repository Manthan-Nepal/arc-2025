from functools import reduce

numbers = [1,2,3,4,5,6,7,8]

even = list(filter(lambda x: x%2 == 0, numbers))
print(even)

square = list(map(lambda x: x*x, even))
print(square)

total = reduce(lambda a,b: a+b, square)
print(total)


# def make_incrementor(n):
#     return lambda x: x + n

# f = make_incrementor(42)
# f(0)
# f(1)