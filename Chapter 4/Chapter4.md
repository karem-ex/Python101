---

# Python Lists

Lists are a fundamental data type in the Python programming language. A list is a mutable sequence, meaning you can modify it after its creation. Lists are often used to store collections of homogeneous items, but they can also hold heterogeneous items, such as dictionaries, tuples, and other objects. Nested lists (lists within lists) are also common.

In this chapter, you will learn the following:
- Creating Lists
- List Methods
- List Slicing
- List Copying

## 1. Creating Lists

There are several ways to create a list. You can construct a list in any of the following ways:
- Using a pair of square brackets with nothing inside creates an empty list: `[]`
- Using square brackets with comma-separated items: `[1, 2, 3]`
- Using a list comprehension (see Chapter 13 for more information): `[x for x in iterable]`
- Using the `list()` function: `list(iterable)`

An iterable is a collection of items that can return its members one at a time; some iterables have an order (i.e., sequences), and some do not. Lists themselves are sequences, and strings are also sequences. You can think of strings as a sequence of characters.

### Example 1: Creating a Simple List

```python
my_list = [1, 2, 3]
print(my_list)
```
Output:
```python
[1, 2, 3]
```

### Example 2: Using `list()` to Create a List

```python
list_of_strings = list('abc')
print(list_of_strings)
```
Output:
```python
['a', 'b', 'c']
```

### Example 3: Creating an Empty List

```python
empty_list = []
print(empty_list)

another_empty_list = list()
print(another_empty_list)
```
Output:
```python
[]
[]
```

## 2. List Methods

Methods allow you to perform operations on a list. Below is a list of common list methods:

- `append()`
- `clear()`
- `copy()`
- `count()`
- `extend()`
- `index()`
- `insert()`
- `pop()`
- `remove()`
- `reverse()`
- `sort()`

### 2.1. Adding to a List

There are three list methods for adding elements:

- **append()**: Adds an item to the end of the list.
- **extend()**: Adds all items from another iterable (e.g., a list) to the current list.
- **insert()**: Adds an item at a specific index.

#### Example: Using `append()`

```python
my_list = ['a', 'b', 'c']
my_list.append(1)
print(my_list)
```
Output:
```python
['a', 'b', 'c', 1]
```

#### Example: Using `insert()`

```python
my_list.insert(0, 'first')
print(my_list)
```
Output:
```python
['first', 'a', 'b', 'c', 1]
```

#### Example: Using `extend()`

```python
my_list = [1, 2, 3]
other_list = [4, 5, 6]
my_list.extend(other_list)
print(my_list)
```
Output:
```python
[1, 2, 3, 4, 5, 6]
```

You can also combine lists using concatenation:

```python
combined = my_list + other_list
print(combined)
```
Output:
```python
[1, 2, 3, 4, 5, 6]
```

### 2.2. Accessing and Changing List Elements

You can access elements of a list using their index, which starts at 0.

#### Example: Accessing Items by Index

```python
my_list = [7, 8, 9]
print(my_list[0])  # Output: 7
print(my_list[2])  # Output: 9
```

#### Example: Negative Indexing

You can use negative indices to access elements from the end of the list.

```python
print(my_list[-1])  # Output: 9
```

### 2.3. Deleting from a List

There are four primary ways to remove items from a list:

- `clear()`: Removes all items from the list.
- `pop()`: Removes and returns an item at the specified index (or the last item if no index is specified).
- `remove()`: Removes the first occurrence of a specific item.
- `del`: Deletes an item at a specified index.

#### Example: Using `clear()`

```python
my_list = [7, 8, 9]
my_list.clear()
print(my_list)
```
Output:
```python
[]
```

#### Example: Using `pop()`

```python
my_list = [7, 8, 9]
removed_item = my_list.pop()
print(removed_item)  # Output: 9
print(my_list)       # Output: [7, 8]
```

#### Example: Using `remove()`

```python
my_list = [7, 8, 9]
my_list.remove(8)
print(my_list)
```
Output:
```python
[7, 9]
```

#### Example: Using `del`

```python
my_list = [7, 8, 9]
del my_list[1]
print(my_list)
```
Output:
```python
[7, 9]
```

### 2.4. Sorting a List

You can sort a list in place using the `sort()` method or return a new sorted list using the `sorted()` function.

#### Example: Using `sort()`

```python
my_list = [4, 10, 2, 1, 23, 9]
my_list.sort()
print(my_list)
```
Output:
```python
[1, 2, 4, 9, 10, 23]
```

#### Example: Using `sorted()`

```python
my_list = [4, 10, 2, 1, 23, 9]
sorted_list = sorted(my_list)
print(sorted_list)
```
Output:
```python
[1, 2, 4, 9, 10, 23]
```

### 2.5. List Slicing

List slicing allows you to access a portion of the list. You can specify a start and stop index, and optionally, a step.

#### Example: Basic Slicing

```python
my_list = [4, 10, 2, 1, 23, 9]
print(my_list[1:3])  # Output: [10, 2]
```

#### Example: Using Negative Indices

```python
print(my_list[-2:])  # Output: [23, 9]
```

#### Example: Omitting Start or Stop

```python
print(my_list[:3])  # Output: [4, 10, 2]
```

### 2.6. Copying a List

You can copy a list using the `copy()` method or list slicing.

#### Example: Using `copy()`

```python
my_list = [1, 2, 3]
new_list = my_list.copy()
print(new_list)
```
Output:
```python
[1, 2, 3]
```

#### Example: Using Slicing

```python
new_list = my_list[:]
print(new_list)
```
Output:
```python
[1, 2, 3]
```

---

## Wrapping Up

You will use lists extensively when programming in Python. In this chapter, you learned how to:

- Create lists
- Use various list methods
- Slice and copy lists
--- 
