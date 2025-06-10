# Write a module named math_utils.py with a function factorial(n). Import and use it in another file.

def factorial(n):
    x= 1
    for i in range(2, n+1):
        x= x*i

    return x

