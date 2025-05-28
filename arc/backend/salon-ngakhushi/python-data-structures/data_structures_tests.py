# List: is mutable so doesn't have a fixed length
name= ['Hiro', 'siro', 'yuro', 'jiro']

# Tuple: is immutable so it is fixed in length
name= ('Hiro', 9339716413, 'Student', 1994)

# List is better for same data types while tuple is better for different data types.

# list() constructor
tuple= list(('Hiro', 9339716413, 'Student', 1994))
print(tuple)

num= list(range(10))
print(num)

even_numbers= [number for number in range (1, 20) if number%2==0]
print(even_numbers)

# dictonary can use tuples as key but not lists.

# zip() inside of dict() can combine list into a dictionary
name= ['Hiro', 'siro', 'yuro', 'jiro']
age= [21, 17, 14, 32]
combine= dict(zip(name, age))
print(combine)

Cars= dict.fromkeys(['Ferari', 'BMW', 'Ford F1', 'Tesla'], 3)
print(Cars)

