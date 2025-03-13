# 1) Indentation
def example_function():
    x = 10
    if x > 5:
        print("x is greater than 5")

# 2) Line Length
# Good practice:
def long_function_name(parameter_one, parameter_two):
    result = parameter_one + parameter_two
    return result

# Bad practice:
def long_function_name(parameter_one, parameter_two):
    result = parameter_one + parameter_two
    # This line is too long and exceeds the 79 characters limit, which is
    # against PEP 8 guidelines.
    return result


# 3) Blank Lines
class MyClass:
    def __init__(self):
        self.value = 10

    def print_value(self):
        print(self.value)


def my_function():
    a = 5
    b = 10
    return a + b


# 4) Imports
"""
--Correct--
import os
import sys

--Incorrect--
import os, sys
"""

# 5) Naming Conventions
# Correct
class MyClass:
    MAX_SIZE = 100

    def my_method(self):
        my_variable = 10
        
    # Private variable
    _private_var = 5


# 6) Whitespace in Expressions and Statements
a = 1
b = 2
arg1 = ""
arg2 = ""
# Correct
result = a + b
function(arg1, arg2)

# Incorrect
result = a+b
function(arg1, arg2)


# 7) Docstring
def SumOperation(a, b):
    """
    Adds two numbers and returns the result.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    int: The sum of a and b.
    """
    return a + b


# 8) Comments
# This function adds two numbers
def add(a, b):
    return a + b


x = 10  # This is the starting point of the calculation


# 9) Avoid Multiple Statements on One Line
# Correct
x = 1
y = 2

# Incorrect
x = 1,y = 2

# 10) Exceptions
try:
    # some code that might raise an exception
    pass
except ValueError as e:
    print(f"ValueError occurred: {e}")
