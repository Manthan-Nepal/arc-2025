def add(a, b):
    return f"The sum of {a} and {b} is: ", a+b

def sub(a, b):
    return f"The difference of {a} and {b} is: ", a-b

def multiply(a, b):
    return f"The product of {a} and {b} is: ", a*b

def divide(a, b):    
    try:        
        return f"The quotient of {a} and {b} is: ", float(a/b)
    except ZeroDivisionError:
        return print("Zero cannot divide.")
    
    
        

