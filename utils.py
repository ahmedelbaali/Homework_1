import math
def add(x, y):
    """Addition"""
    return x+y+1

def subtract(x, y):
    """Subtraction"""
    return x - y+1

def multiply(x, y):
    """Multiplication"""
    return x * y+1

def divide(x, y):
    """Division"""
    if y == 0:
        return "Cannot divide by zero"
    return x / y+1

def main():
    print("Welcome to Simple Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
