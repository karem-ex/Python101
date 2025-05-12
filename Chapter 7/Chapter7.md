A set data type is defined as an “unordered collection of distinct hashable objects” according
to the Python 3 documentation. You can use a set for membership testing, removing duplicates
from a sequence and computing mathematical operations, like intersection, union, difference, and
symmetric difference.

Due to the fact that they are unordered collections, a set does not record element position or order of
insertion. Because of that, they also do not support indexing, slicing or other sequence-like behaviors
that you have seen with lists and tuples.


There are two types of set built-in to the Python language:
• set - which is mutable
• frozenset - which is immutable and hashable


This chapter will focus on set.
You will learn how to do the following with sets:
• Creating a set
• Accessing set members
• Changing items
• Adding items
• Removing items
• Deleting a set

Let’s get started by creating a set!
---

# Python Sets

A set is a collection data type in Python that is unordered, mutable, and does not allow duplicate elements.

## 1. Introduction to Sets

* Sets are defined using curly braces `{}` or the `set()` constructor.
* Sets automatically remove duplicate values.

### Example:

```python
my_set = {1, 2, 3}
```

## 2. Creating a Set

### Using Curly Braces

```python
my_set = {1, 2, 3, 4}
```

### Using the `set()` Constructor

```python
my_set = set([1, 2, 3, 4])
```

### Empty Set

```python
empty_set = set()  # Note: {} creates an empty dictionary, not a set!
```

## 3. Accessing Set Members

Sets do not support indexing, slicing, or other sequence-like behavior. However, you can loop through sets or use the `in` keyword to check membership.

### Example:

```python
my_set = {1, 2, 3, 4}

# Looping through a set
for item in my_set:
    print(item)

# Checking membership
if 2 in my_set:
    print("2 is in the set")
```

## 4. Changing Set Items

Sets are mutable, meaning you can add and remove items, but individual elements cannot be accessed or changed directly by index.

### Example:

```python
my_set = {1, 2, 3}

# Adding new items (covered in next section)
my_set.add(4)

# Removing items (covered in next section)
my_set.remove(2)
```

## 5. Adding Items to a Set

### `add()` Method

Adds a single item to the set.

```python
my_set.add(5)
```

### `update()` Method

Adds multiple items (iterable like list, tuple) to the set.

```python
my_set.update([6, 7, 8])
```

### Example:

```python
my_set = {1, 2, 3}
my_set.add(4)  # Adding single element
my_set.update([5, 6, 7])  # Adding multiple elements
```

## 6. Removing Items from a Set

### `remove()` Method

Removes an item from the set. If the item is not found, it raises a `KeyError`.

```python
my_set.remove(2)  # Removes 2 from the set
```

### `discard()` Method

Removes an item from the set, but does not raise an error if the item is not found.

```python
my_set.discard(10)  # Does nothing if 10 is not in the set
```

### `pop()` Method

Removes and returns an arbitrary element from the set. Since sets are unordered, the element removed is random.

```python
item = my_set.pop()
```

### `clear()` Method

Removes all elements from the set.

```python
my_set.clear()  # The set is now empty
```

## 7. Deleting a Set

To delete a set completely, use the `del` keyword.

```python
del my_set
# Now my_set no longer exists
```

## 8. Set Operations

### Union

Combines elements from two sets, excluding duplicates.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # or set1.union(set2)
```

### Intersection

Returns elements that are present in both sets.

```python
intersection_set = set1 & set2  # or set1.intersection(set2)
```

### Difference

Returns elements present in the first set but not in the second.

```python
difference_set = set1 - set2  # or set1.difference(set2)
```

### Symmetric Difference

Returns elements present in either of the sets, but not in both.

```python
sym_diff_set = set1 ^ set2  # or set1.symmetric_difference(set2)
```

## 9. Set Methods

* `add()`: Adds an element to a set.

```python
my_set.add(5)
```

* `remove()`: Removes an element from a set. Throws a KeyError if element is not found.

```python
my_set.remove(3)
```

* `discard()`: Removes an element from a set, but does not raise an error if not found.

```python
my_set.discard(10)  # no error even if 10 is not in the set
```

* `clear()`: Removes all elements from a set.

```python
my_set.clear()
```

* `copy()`: Returns a shallow copy of the set.

```python
new_set = my_set.copy()
```

## 10. Set Properties

* **Unordered**: Elements do not have a specific order.
* **Immutable**: Elements within a set must be immutable, but the set itself is mutable.
* **Unique**: No duplicate elements allowed.

## 11. Set Comprehension

Sets can be created using comprehension syntax similar to list comprehension.

```python
squares = {x**2 for x in range(6)}  # {0, 1, 4, 9, 16, 25}
```

---

