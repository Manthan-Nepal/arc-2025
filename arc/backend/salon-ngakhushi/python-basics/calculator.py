def CLI_Calculator (a, b):
    operation= int(input("\nWhat Operation would you like to perform?\n1. Add\n2. Subttract\n3. Multiply\n4. Divide\nAnwer: "))
    if operation== 1:
        print("The sum of "+str(a)+" and "+str(b)+" is: ", a+b)
    elif operation== 2:
        print("The difference of "+str(a)+" and "+str(b)+" is: ", a-b)
    elif operation== 3:
        print("The product of "+str(a)+" and "+str(b)+" is: ", a*b)
    elif operation== 4:
        print("The quotient of "+str(a)+" and "+str(b)+" is: ", float(a/b))
    else:
        print("Invalid input.")
    return again(a,b)    
    
def again(a,b):
    firstnum= a
    secondnum= b
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