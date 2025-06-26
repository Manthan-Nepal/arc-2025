import calculator_module
from calculator_module import add, sub, multiply, divide

def CLI_Calculator (a, b):
    operation= int(input("\nWhat Operation would you like to perform?\n1. Add\n2. Subttract\n3. Multiply\n4. Divide\nAnwer: "))
    if operation== 1:
        add(a, b)
    elif operation== 2:
        sub(a, b)
    elif operation== 3:
        multiply(a, b)
    elif operation== 4:
        divide(a, b)
    else:
        print("Invalid input.")
    return again(a, b)    
    
def again(a, b):
    print("\nWelcome to a CLI Calculator!")
    firstnum, secondnum= a, b
    answer= int(input("\nWould you like to perform another operation?\n1. Yes\n2. No\n3. Start over\nAnswer: "))
    if answer== 1:
        CLI_Calculator(firstnum, secondnum)
    elif answer== 2:
        exit()
    elif answer== 3:
        user_input()
    else:
        print("Invalid input.")
        again(firstnum, secondnum)
        
def user_input():
    firstnum= int(input("\nEnter the first number: "))
    secondnum= int(input("Enter the second number: "))
    CLI_Calculator(firstnum, secondnum)

user_input()
