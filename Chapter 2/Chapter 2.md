You will be using strings very often when you program. A string is a series of letters surrounded by single, double, or triple quotes. Python 3 defines a string as a “Text Sequence Type.” You can cast other types to a string using the built-in `str()` function.

In this chapter, you will learn how to:

- Create strings
- Use string methods
- Format strings
- Concatenate strings
- Slice strings

Let’s get started by learning the different ways to create strings!

## 1. Creating Strings

Here are some examples of creating strings:

```python
name = 'Mike'
first_name = 'Mike'
last_name = "Driscoll"
triple = """multi-line string"""
```

Here is an example of converting an integer to a string:

```python
number = 5
str(number)
print(type(number))
```

In Python, backslashes can be used to create escape sequences. Here are a couple of examples:

- `\b` - backspace
- `\n` - line feed
- `\r` - ASCII carriage return
- `\t` - tab

## 2. String Methods

In Python, everything is an object. You will learn how useful this can be in chapter 18 when you learn about introspection. For now, just know that strings have methods (or functions) that you can call on them.

Here are three examples:

```python
name = 'mike'
print(name.capitalize())  # 'Mike'
print(name.upper())       # 'MIKE'
print('MIke'.lower())     # 'mike'
```

The method names give you a clue as to what they do. For example, `.capitalize()` will change the first letter in the string to a capital letter.

To get a full listing of the methods and attributes that you can access, you can use Python’s built-in `dir()` function:

```python
dir(name)
```

Example output:

```python
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', ... , 'capitalize', 'casefold', 'center', ... , 'zfill']
```

The first third of the listing are special methods that are sometimes called “dunder methods” (AKA double-underscore methods) or “magic methods.” You can ignore these for now as they are used more for intermediate and advanced use-cases. The items in the list above that don’t have double-underscores at the beginning are the ones that you will probably use the most.

You will find that the `.strip()` and `.split()` methods are especially useful when parsing or manipulating text.

You can use `.strip()` and its variants, `.rstrip()` and `.lstrip()`, to strip off white space from the string, including tab and newline characters. This is especially useful when you are reading in a text file that you need to parse.

In fact, you will often end up stripping end-of-line characters from strings and then using `.split()` on the result to parse out sub-strings.

### Example: Parsing a String

Let’s do a little exercise where you will learn how to parse out the 2nd word in a string.

To start, here’s a string:

```python
my_string = 'This is a string of words'
```

Now, to get the parts of a string, you can call `.split()`:

```python
my_string.split()  # ['This', 'is', 'a', 'string', 'of', 'words']
```

The result is a list of strings. You can use list indexing to get the second element:

```python
'This is a string of words'.split()[1]  # 'is'
```

When doing string parsing for work, I personally have found that you can use the `.strip()` and `.split()` methods effectively to get almost any data you need. Occasionally, you might need to use Regular Expressions (regex), but most of the time these two methods are enough.

## 3. String Formatting

String formatting or string substitution is where you have a string that you would like to insert into another string. This is especially useful when you need to create a template, such as a form letter. You will also use string substitution a lot for debugging output, printing to standard out, and much more.

Standard out (or `stdout`) is a term used for printing to the terminal. When you run your program from the terminal and you see output from your program, that is because your program “prints” to standard out or standard error (`stderr`).

Python has three different ways to accomplish string formatting:

- Using the `%` Method
- Using `.format()`
- Using formatted string literals (f-strings)

### Formatting Strings Using `%s` (printf-style)

This type of formatting can be quirky to work with and has been known to lead to common errors such as failing to display Python tuples and dictionaries correctly. Using either of the other two methods is preferred in that case.

`%s` means convert any Python object to a string using `str()`.

Here are some basic argument specifiers you should know:

- `%s` - String (or any object with a string representation, like numbers)
- `%d` - Integers
- `%f` - Floating point numbers
- `%.(number of digits)f` - Floating point numbers with a fixed amount of digits to the right of the dot. Example: `%.2f`
- `%x`/`%X` - Integers in hex representation (lowercase/uppercase)

Here is an example:

```python
name = 'Mike'
print('My name is %s' % name)  # My name is Mike
```

### Formatting Strings Using `.format()`

Python strings have supported the `.format()` method for a long time.

Let’s take a look at a few short examples to see how `.format()` works:

```python
age = 18
name = 'Mike'
print('Hello {}. You must be at least {} to continue!'.format(name, age))
# Output: Hello Mike. You must be at least 18 to continue!
```

### Formatting Strings with f-strings

Formatted string literals or f-strings are strings that have an “f” at the beginning and curly braces inside of them that contain expressions. These expressions tell the f-string about any special processing that needs to be done to the inserted string, such as justification, float precision, etc.

Let’s look at a simple example:

```python
name = 'Mike'
age = 20
print(f'Hello {name}. You are {age} years old')  
# Output: Hello Mike. You are 20 years old
```

### Notes:
- If you create an f-string with empty braces, you will get a syntax error:

```python
f'Hello {}. You are {} years old'  # SyntaxError: f-string: empty expression not allowed
```

## 4. String Concatenation

Strings also allow concatenation, which is a fancy word for joining two strings into one. To concatenate strings together, you can use the `+` sign:

```python
first_string = 'My name is'
second_string = 'Mike'
print(first_string + ' ' + second_string)  # Output: My name is Mike
```

Another way to merge strings is to use the `.join()` method. The `.join()` method accepts an iterable, such as a list, of strings and joins them together:

```python
first_string = 'My name is'
second_string = 'Mike'
print(' '.join([first_string, second_string]))  # Output: My name is Mike
```

More often than not, you can use an f-string rather than concatenation or `.join()`, and the code will be easier to follow.

## 5. String Slicing

Slicing in strings works in much the same way that it does for Python lists. Let’s take the string "Mike". The letter "M" is at position 0 and the letter "e" is at position 3.

If you want to grab characters 0-3, you would use this syntax: `my_string[0:4]`

This means you want the substring starting at position 0 up to but not including position 4.

Here are a few examples:

```python
'this is a string'[0:4]  # Output: 'this'
'this is a string'[:4]   # Output: 'this'
'this is a string'[-4:]  # Output: 'ring'
```

## Wrapping Up

Python strings are powerful and useful. They can be created using single, double, or triple quotes. Strings are objects, so they have methods. You also learned about string concatenation, string slicing, and three different methods of string formatting.

The newest flavor of string formatting is the f-string. It is also the most powerful and the currently preferred method for formatting strings.
```
