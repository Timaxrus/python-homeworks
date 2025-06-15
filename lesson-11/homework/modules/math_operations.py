# math_operations.py

def add(a, b):
    """
    Adds two numbers and returns the result.
    """
    return a + b

def subtract(a, b):
    """
    Subtracts the second number from the first and returns the result.
    """
    return a - b

def multiply(a, b):
    """
    Multiplies two numbers and returns the result.
    """
    return a * b

def divide(a, b):
    """
    Divides the first number by the second number and returns the result.
    Handles division by zero by returning an error message.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."