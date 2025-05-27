def user_input():
    x= int(input("How many numbers would you like to enter?\nAnswer: "))
    numbers= []
    for i in range(x):
        num= int(input("Enter a number: "))
        numbers.append(num)
        print("Even numbers: ", [element for element in numbers if element%2==0])
        
user_input()