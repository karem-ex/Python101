```markdown
# Python Numeric Types

Python is a little different than some languages in that it only has three built-in numeric types. A built-in data type means that you don’t have to do anything to use them other than typing out their name.

The built-in numeric types are:
- `int`
- `float`
- `complex`

## 1. Integers

You can create an integer in two ways in Python. The most common way is to assign an integer to a variable:

```python
my_integer = 3
```

The equals sign (`=`) is Python’s assignment operator. It “assigns” the value on the right to the variable name on the left. So in the code above, you are assigning the value `3` to the variable `my_integer`.

The other way to create an integer is to use the `int()` callable, like this:

```python
my_integer = int(3)
```

Most of the time, you won’t use `int()` to create an integer. In fact, `int()` is usually used for converting a string or other type to an integer. Another term for this is **casting**.

A little known feature about `int()` is that it takes an optional second argument for the base in which the first argument is to be interpreted. In other words, you can tell Python to convert to base2, base8, base16, etc.

Here’s an example:

```python
int('10', 2)  # Output: 2
int('101', 2)  # Output: 5
```

The first argument has to be a string, while the second argument is the base, which in this case is `2`.

## 2. Floats

A `float` in Python refers to a number that has a decimal point in it. For example, `2.0` is a float while `2` is an `int`.

You can create a float in Python like this:

```python
my_float = 2.0
```

This code will assign the number, `2.0`, to the variable `my_float`.

You can also create a float like this:

```python
my_float = float(2.0)
```

> **Note:** The `float` numeric type is inexact and may differ across platforms. You shouldn’t use the `float` type when dealing with sensitive numeric types, such as money values, due to rounding issues. Instead, it is recommended that you use Python’s `decimal` module.

## 3. Complex Numbers

A complex number has a real and an imaginary part, which are each a floating-point number. Let’s look at an example with a complex number object named `comp` to see how you can access each of these parts by using `comp.real` and `comp.imag` to extract the real and imaginary parts, respectively:

```python
comp = 1 + 2j
type(comp)  # Output: <class 'complex'>
comp.real  # Output: 1.0
comp.imag  # Output: 2.0
```

In the code sample above, you created a complex number. To verify that it is a complex number, you can use Python’s built-in `type()` function on the variable. Then you extract the real and imaginary parts from the complex number.

You can also use the `complex()` built-in callable to create a complex number:

```python
complex(10, 12)  # Output: (10+12j)
```

Here you created a complex number in the interpreter, but you don’t assign the result to a variable.

## 4. Numeric Operations

All the numeric types, with the exception of complex, support a set of numeric operations.

Here is a list of the operations that you can do:

| Operation     | Result                                      |
|---------------|---------------------------------------------|
| `a + b`       | The sum of `a` and `b`                      |
| `a - b`       | The difference of `a` and `b`               |
| `a * b`       | The product of `a` and `b`                  |
| `a / b`       | The quotient of `a` and `b`                 |
| `a // b`      | The floored quotient of `a` and `b`         |
| `a % b`       | The remainder of `a / b`                    |
| `-a`          | `a` negated (multiply by -1)                |
| `+a`          | `a` unchanged                               |
| `abs(a)`      | absolute value of `a`                       |
| `int(a)`      | `a` converted to integer                    |
| `float(x)`    | `a` converted to a floating-point number    |
| `complex(re, im)` | A complex number with real and imaginary |
| `c.conjugate()` | The conjugate of the complex number `c`     |
| `divmod(a, b)`  | The pair: `(a // b, a % b)`                |
| `pow(a, b)`   | `a` to the power of `b`                     |
| `a ** b`      | `a` to the power of `b`                     |

## 5. Augmented Assignment

Python supports doing some types of arithmetic using a concept called **Augmented Assignment**.

This idea was first proposed in PEP 203:
- [PEP 203](https://www.python.org/dev/peps/pep-0203/)

The syntax allows you to do various arithmetic operations using the following operators:
- `+=` 
- `-=` 
- `*=` 
- `/=`
- `%=` 
- `**=`
- `<<=` 
- `>>=` 
- `&=`
- `^=`
- `|=`

This syntax is a shortcut for doing common arithmetic in Python. With it you can replace the following code:

```python
x = 1
x = x + 2
print(x)  # Output: 3
```

with this:

```python
x = 1
x += 2
print(x)  # Output: 3
```

This code is the equivalent of the previous example.

## Wrapping Up

In this chapter, you learned the basics of Python’s Numeric types. Here you learned a little about how Python handles `int`, `float`, and `complex` number types. You can use these types for working with most operations that involve numbers. However, if you are working with floating-point numbers that need to be precise, you will want to check out Python’s `decimal` module. It is tailor-made for working with that type of number.
```
