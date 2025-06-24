num1 = float(input("Enter first number: "))
op = input("Operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print("cant divide by zer0")
    
else:
    print("Invalid operator")