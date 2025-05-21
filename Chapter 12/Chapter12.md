### What are Exceptions?

An **exception** is an event that can disrupt the normal flow of the program. It is usually an error that Python detects while the program is running, like dividing by zero, trying to access a non-existent file, or using invalid data types in a function.

### The Basic Structure: `try` and `except`

The basic way to handle exceptions is with the `try` and `except` blocks. Here's the structure:

```python
try:
    # Code that may raise an exception
    risky_code()
except SomeException:
    # Code to handle the exception
    print("An error occurred!")
```

* **`try`**: This block contains the code that might raise an exception.
* **`except`**: This block handles the exception if it occurs.

### Example: Basic Exception Handling

Let’s take a simple example where we try to divide by zero. This will raise an exception:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
```

Here, `ZeroDivisionError` is the specific exception that happens when you try to divide by zero. The `except` block catches this error and prints a message.

### Catching Multiple Exceptions

Sometimes, there are multiple types of errors that could happen in the `try` block. You can catch different exceptions by specifying multiple `except` blocks.

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("That's not a valid number!")
```

In this example:

* If the user enters a non-numeric value, a `ValueError` will be raised.
* If the user enters `0`, a `ZeroDivisionError` will be raised.

### The `else` Block

You can also add an `else` block after the `except` block. This block of code runs if no exception was raised.

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("That's not a valid number!")
else:
    print(f"Result is {result}")
```

Here, if there’s no exception (i.e., the input is a valid number and not zero), the `else` block will execute and print the result.

### The `finally` Block

The `finally` block will always run, no matter whether there was an exception or not. It’s typically used for cleaning up resources (like closing a file or a network connection).

```python
try:
    file = open("myfile.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
else:
    print(content)
finally:
    print("This will always run.")
    # It's good practice to close the file
    if 'file' in locals():
        file.close()
```

Even if there’s an error opening the file, the `finally` block will execute. This is useful for cleanup actions.

### Raising Exceptions Manually

You can also raise exceptions intentionally using the `raise` keyword. For example, if you want to check some conditions and raise an exception when needed:

```python
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older.")
    else:
        print("Age is valid.")

try:
    check_age(16)
except ValueError as e:
    print(f"Error: {e}")
```

Here, if the age is less than 18, we manually raise a `ValueError` with a custom message.

---

### Summary of Key Concepts:

* **`try`**: Block where you write the code that may cause an exception.
* **`except`**: Block that catches the exception and handles it.
* **`else`**: Runs if no exception occurs.
* **`finally`**: Runs no matter what, useful for cleanup actions.
* **`raise`**: You can manually raise exceptions when needed.

---

