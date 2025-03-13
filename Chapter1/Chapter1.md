Chapter 1 - Documenting Your Code

    Documenting your code early on is quite a bit more important than most new developers realize. 
    Documentation in software development refers to the idea of giving your variables, functions and other identifiers descriptive names. 
    It also refers to adding good comments. When you are immersed in developing your latest creation, it is easy to create variables and functions with non-descriptive names.
    A month or a year later, when you inevitably come back to your code, you will spend an inordinate amount of time trying to figure out what your code does. 
    By making your code self-documenting and adding comments when necessary, you will make your code more readable for yourself and for anyone else who may use your code. 
    This will make updating your code and refactoring your code easier too!

In this chapter you will learn about the following topics:
• Comments
• Docstrings
• PEP8 - The Python Style Guide


What is Comments ?

    Comments are lines of explanation that belong to you, not your computer.


What is Docstrings ?

    In Python, a docstring is a special type of string used to document your code. 
    It provides a way to describe what a function, class, or module does. 
    The docstring is placed immediately after the definition of a function, method, class, or module, and is enclosed in triple quotes (""" """ or ''' ''').


    Key points about docstrings:

    Placement: Docstrings should be the first statement inside a function, method, class, or module.

    Multiline: You can use triple quotes to write multi-line docstrings.

    Accessing: You can access a function’s or class's docstring using the .__doc__ attribute.

    In Summary: docstrings are an essential part of writing clean, understandable, and maintainable Python code.


What is PEP8 ?
    
    PEP 8 is Python's Style Guide for Python Code. 
    It provides conventions and recommendations for writing Python code in a way that promotes readability and consistency across the Python community. 
    PEP 8 stands for Python Enhancement Proposal 8 and is widely regarded as the standard guide for writing clean, maintainable Python code.

    PEP 8: Python Style Guide - Key Points

    1-Indentation:
        Use 4 spaces per indentation level.
        Do not use tabs.

    2-Line Length:
        Limit all lines to 79 characters.
        Docstrings: Limit to 72 characters per line.

    3-Blank Lines:
        2 blank lines before top-level functions and class definitions.
        1 blank line between methods in a class.

    4-Imports:
        Imports should be on separate lines.
        Order imports:
            Standard library imports
            Third-party imports
            Local imports

    5-Naming Conventions:
        Variables/Functions: Use snake_case (lowercase with underscores).
        Classes: Use CamelCase (PascalCase).
        Constants: Use UPPERCASE_SNAKE_CASE.
        Private variables/functions: Prefix with _.

    6-Whitespace in Expressions and Statements:
        Add single spaces around operators and after commas.
        Avoid spaces in function calls and indexing (e.g., my_function(arg)).

    7-Docstrings:
        Use docstrings for all public classes, methods, and functions.
        Docstrings should be enclosed in triple quotes (""" """).

    8-Comments:
        Write comments as complete sentences.
        Use block comments for explanations and inline comments for short clarifications.
        Start comments with a capital letter, unless it’s a comment within a code block.

    9-Avoid Multiple Statements on One Line:
        Do not write multiple statements on a single line.
        Example: x = 1; y = 2 is discouraged. 
        Write as:
            x = 1
            y = 2
    10-Exceptions:

    Be explicit when catching exceptions, i.e., except ValueError as e:.
