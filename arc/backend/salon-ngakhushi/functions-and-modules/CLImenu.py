import math_operations as mops

def operate(a, b):
    operation= int(input("What operation would you like to perform?\n1. Add\n2. Subtract\nAnswer: "))

    if operation==1:
        mops.add(a, b)
        again(operation)
    elif operation==2:
        mops.subtract(a, b)
        again(operation)
    else:
        print("Invalid option: Choose a given option")
        operate(a, b)
    
    
def again(x):
    if x==1:
        print("Would you like to perform Subtraction with the same numbers?")
        option= int(input("Answer: "))
    elif x==2:
        print("Would you like to perform Addition with the same numbers?")
        option= int(input("Answer: "))
    else:
        print("Invalid option.")
        

def display():        
    print("\n---Welcome to the Add or Subtract Menu---")
    a= int(input("Enter first number: "))
    b= int(input("Enter second number: "))
    print()
    operate(a,b)

display()