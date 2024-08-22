"""
Calculator functions
"""


def add(x, y):
    """Add two numbers together"""
    return x + y


def sub(x, y):
    """Subtract the second number from the first"""
    return x - y


def div(x, y):
    """Divide x by y"""
    if y == 0:
        raise ValueError('Cannot divide by zero!')
    return x / y
