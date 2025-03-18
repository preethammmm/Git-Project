# scientific_calculator.py
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

def power(a, b):
    return math.pow(a, b)

def sqrt(a):
    return math.sqrt(a)

def sin(a):
    return math.sin(math.radians(a))

def cos(a):
    return math.cos(math.radians(a))

def tan(a):
    return math.tan(math.radians(a))

def main():
    print("Scientific Calculator")
    print("Available operations: +, -, *, /, power, sqrt, sin, cos, tan")
    op = input("Enter operation: ")
    
    if op in ['+', '-', '*', '/', 'power']:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if op == '+':
            print("Result:", add(a, b))
        elif op == '-':
            print("Result:", subtract(a, b))
        elif op == '*':
            print("Result:", multiply(a, b))
        elif op == '/':
            print("Result:", divide(a, b))
        elif op == 'power':
            print("Result:", power(a, b))
    elif op in ['sqrt', 'sin', 'cos', 'tan']:
        a = float(input("Enter number: "))
        if op == 'sqrt':
            print("Result:", sqrt(a))
        elif op == 'sin':
            print("Result:", sin(a))
        elif op == 'cos':
            print("Result:", cos(a))
        elif op == 'tan':
            print("Result:", tan(a))
    else:
        print("Invalid operation")

if __name__ == '__main__':
    main()
