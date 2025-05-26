def OddorEven(a):
    if a%2!=0:
        print("{a} is odd.")
    else:
        print("{a} is even.")
    again= int(input("\nWould you like to Enter another number?\n1. Yes\n2. No\nAnswer: "))
    if again== 1:
        user_input()
    elif again== 2:
        exit()

def user_input():
    print("\nWelcome to Odd and Even number sorter!")
    number= int(input("Enter a number: "))
    OddorEven(number)
    
   
user_input()
