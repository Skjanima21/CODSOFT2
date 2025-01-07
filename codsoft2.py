def calculator():
    print("Welcome to the Simple Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    try:
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        if operation == "+":
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")
        elif operation == "*":
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result}")
        elif operation == "/":
            if num2 == 0:
                print("\nError: Division by zero is not allowed!")
            else:
                result = num1 / num2
                print(f"\nResult: {num1} / {num2} = {result}")
        else:
            print("\nInvalid operation. Please choose +, -, *, or /.")
    except ValueError:
        print("\nError: Please enter valid numbers.")
if __name__ == "__main__":
    calculator()
