import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def square(num):
    return num ** 2

def square_root(num):
    if num >= 0:
        return math.sqrt(num)
    else:
        return "Error: Negative input for square root"

def logarithm(num):
    if num > 0:
        return math.log(num)
    else:
        return "Error: Logarithm undefined for non-positive values"

while True:
    print("Calculator App")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Square Root")
    print("7. Logarithm")
    choice = input("Enter choice (1-7): ")

    if choice in ['1','2','3','4']:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        if choice =='1':
            print("Result:", add(num1, num2))
        elif choice =='2':
            print("Result:", subtract(num1, num2))
        elif choice =='3':
            print("Result:", multiply(num1, num2))
        elif choice =='4':
            print("Result:", divide(num1, num2))

    elif choice in ['5','6','7']:
        num = int(input("Enter number: "))

        if choice =='5':
            print("Result:", square(num))
        elif choice =='6':
            print("Result:", square_root(num))
        elif choice =='7':
            print("Result:", logarithm(num))

    else:
        print("Invalid input")

    continue_choice = input("Do you want to perform another calculation? (yes/no): ").lower()
    if continue_choice != 'yes':
        print("Goodbye!")
        break

