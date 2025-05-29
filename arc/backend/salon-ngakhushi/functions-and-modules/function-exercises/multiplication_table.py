# Write a program to pring multiplication table of a number given by user.

def user_in():
    inp= int(input("Enter the number: "))
    j=1
    for i in range(1, 11):
        print(f"{inp}x{j} = ", inp*j)
        j+=1
        
user_in()