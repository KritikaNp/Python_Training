import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Square root of negative number."
    return math.sqrt(x)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def calculator():
    print("****ADVANCED CALCULATOR****")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    
    while True:
        choice = input("Enter choice (1-9) or 'q' to quit: ")

        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {exponentiate(num1, num2)}")

        elif choice in ['6', '7', '8', '9']:
            num = float(input("Enter the number (in degrees for trigonometric functions): "))

            if choice == '6':
                print(f"Square root of {num} = {square_root(num)}")
            elif choice == '7':
                print(f"Sine of {num} = {sine(num)}")
            elif choice == '8':
                print(f"Cosine of {num} = {cosine(num)}")
            elif choice == '9':
                print(f"Tangent of {num} = {tangent(num)}")
        else:
            print("Invalid input. Please enter a number between 1-9 or 'q' to quit.")

if __name__ == "__main__":
    calculator()