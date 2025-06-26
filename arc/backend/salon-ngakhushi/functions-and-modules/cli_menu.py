import math_operations as mops
from math_operations import add, subtract

def operate(a, b):
    v1, v2= a, b
    operation= int(input("What operation would you like to perform?\n1. Add\n2. Subtract\nAnswer: "))

    if operation==1:
        add(a, b)
        return again(operation, v1, v2)
    elif operation==2:
        subtract(a, b)
        return again(operation, v1, v2)
    else:
        print("\nInvalid option: Choose a given option")
        return operate(a, b)
    
    
def again(x, a, b):
    if x==1:
        print("\nWould you like to perform Subtraction with the same numbers?")
        option_to_sub= int(input("1. Yes\n2. No\nAnswer: "))
             
        if option_to_sub==1:
            subtract(a,b)
            print("\nWould you like to use different numbers?")
            y= int(input("1. Yes\n2. No\nAnswer: "))        
        else:
            print("\nWould you like to use different numbers?")
            y= int(input("1. Yes\n2. No\nAnswer: "))
            
    elif x==2:
        print("\nWould you like to perform Addition with the same numbers?")
        option_to_add= int(input("1. Yes\n2. No\nAnswer: "))
        
        if option_to_add==1:
            add(a,b)
            print("\nWould you like to use different numbers?")
            y= int(input("1. Yes\n2. No\nAnswer: "))
        else:
            print("\nWould you like to use different numbers?")
            y= int(input("1. Yes\n2. No\nAnswer: "))
    
    else:
        print("\nWould you like to use different numbers?")
        y= int(input("1. Yes\n2. No\nAnswer: "))
        
    if y== 1:
        return display()
    else:
        exit()


def display():        
    print("\n---Welcome to the Add or Subtract Menu---")
    a= int(input("Enter first number: "))
    b= int(input("Enter second number: "))
    print()
    return operate(a,b)

display()
