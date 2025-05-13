# Python Conditional Statements

### 1. **Comparison Operators**

Comparison operators allow us to compare two values, and they typically return either `True` or `False`.

| Operator | Meaning                  | Example           |
| -------- | ------------------------ | ----------------- |
| `==`     | Equal to?                | `5 == 5` → `True` |
| `!=`     | Not equal to?            | `5 != 3` → `True` |
| `>`      | Greater than?            | `5 > 3` → `True`  |
| `<`      | Less than?               | `3 < 5` → `True`  |
| `>=`     | Greater than or equal to | `5 >= 5` → `True` |
| `<=`     | Less than or equal to    | `3 <= 5` → `True` |

**Example Usage:**

```python
x = 10
y = 20

print(x == y)  # False, because 10 is not equal to 20
print(x < y)   # True, because 10 is less than 20
```

---

### 2. **Creating a Simple Conditional**

Conditional statements start with the `if` keyword and check a condition. If the condition is true, a specific action is performed.

**Example:**

```python
x = 10
if x > 5:
    print("x is greater than 5!")
```

Here, the condition checks if `x` is greater than 5. If true, `"x is greater than 5!"` will be printed.

---

### 3. **Branching Conditional Statements**

Branching means checking multiple conditions. This is done using the `if`, `elif`, and `else` keywords.

**Example:**

```python
x = 10

if x > 15:
    print("x is greater than 15.")
elif x > 5:
    print("x is between 5 and 15.")
else:
    print("x is less than 5.")
```

In this example:

* The first condition (`x > 15`) is false, so the second condition is checked.
* Since `x` is between 5 and 15, the second condition is true, and `"x is between 5 and 15."` is printed.

---

### 4. **Nesting Conditionals**

A conditional expression can be placed inside another conditional expression. This is called "nested conditionals."

**Example:**

```python
x = 10

if x > 5:
    if x < 15:
        print("x is between 5 and 15.")
    else:
        print("x is greater than 15.")
else:
    print("x is less than 5.")
```

Here, the outer condition (`x > 5`) is checked first. If true, the inner condition (`x < 15`) is checked.

---

### 5. **Logical Operators**

Logical operators allow you to combine multiple conditions. Python has 3 main logical operators:

* `and`: Both conditions must be true for the result to be true.
* `or`: At least one condition must be true for the result to be true.
* `not`: Reverses the truth value of the condition.

**Example:**

```python
x = 10
y = 5

# and example
if x > 5 and y < 10:
    print("x is greater than 5 and y is less than 10.")

# or example
if x > 15 or y < 10:
    print("x is greater than 15 or y is less than 10.")

# not example
if not x == 10:
    print("x is not equal to 10.")
else:
    print("x is equal to 10.")
```

---

### 6. **Special Operators**

Python also has some special operators, and the most important ones are:

* `is`: Checks whether two objects are the same (not just their values, but their references).
* `is not`: Reverses the check and ensures the objects are not the same.

**Example:**

```python
x = [1, 2, 3]
y = x

if x is y:
    print("x and y refer to the same object.")

z = [1, 2, 3]
if x is not z:
    print("x and z are different objects.")
```

---

