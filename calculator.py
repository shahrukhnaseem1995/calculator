"""
calculator.py
A simple calculator module with basic math operations.
"""

def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the division of a by b. Raises error if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b