# Define a function that accepts any number of numbers and returns their average.

numbers= [12, 2, 4, 5, 7, 35, 90]

def sum(numbers):
    total= 0
    for i in numbers:
        total+= i
    return total

def average(x):
    avg= sum(x)/len(x)
    print(f"Average: {avg:.2f}")

average(numbers)