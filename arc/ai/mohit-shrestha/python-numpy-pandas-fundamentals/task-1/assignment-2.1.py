def add(a:int|float, b:int|float) -> float:
    return a + b

def subtract(a:int|float, b:int|float) -> float:
    return a - b

def multiply(a:int|float, b:int|float) -> float:
    return a * b

def divide(a:int|float, b:int|float) -> float:
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def power(a:int|float, b:int|float) -> float:
    return a ** b

def modulus(a:int|float, b:int|float) -> float:
    if b == 0:
        return "Error: Cannot perform modulus with zero!"
    return a % b


def get_user_input():
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            return a, b
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def main():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Modulus")
        print("7. Exit")

        choice = input("Select an operation (1-7): ")

        if choice == '7':
            print("Exiting the calculator. Thank you.")
            break

        a, b = get_user_input()

        if choice == '1':
            print("Result:", add(a, b))
        elif choice == '2':
            print("Result:", subtract(a, b))
        elif choice == '3':
            print("Result:", multiply(a, b))
        elif choice == '4':
            print("Result:", divide(a, b))
        elif choice == '5':
            print("Result:", power(a, b))
        elif choice == '6':
            print("Result:", modulus(a, b))
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    main()