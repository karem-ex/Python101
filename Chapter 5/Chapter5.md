````markdown
# Python Tuples

Tuples are another sequence type in Python. Tuples consist of a number of values that are separated by commas. 
A tuple is immutable whereas a list is not. Immutable means that the tuple has a fixed value and cannot change. 
You cannot add or delete items in a tuple. Immutable objects are useful when you need a constant hash value.

In this chapter, you will learn how to:

- Create tuples
- Work with tuples
- Concatenate tuples
- Special case tuples

## 1. Creating Tuples

You can create tuples in several different ways. Let’s take a look:

```python
a_tuple = 4, 5
type(a_tuple)
````

Output:

```python
<class 'tuple'>
```

One of the simplest methods of creating a tuple is to have a sequence of values separated by commas. Those values could be integers, lists, dictionaries, or any other object.

Depending on where in the code you are trying to create a tuple, just using commas might be ambiguous; you can always use parentheses to make it explicit:

```python
a_tuple = (2, 3, 4)
type(a_tuple)
```

Output:

```python
<class 'tuple'>
```

However, parentheses by themselves do not make a tuple!

```python
not_a_tuple = (5)
type(not_a_tuple)
```

Output:

```python
<class 'int'>
```

You can cast a list into a tuple using the `tuple()` function:

```python
a_tuple = tuple(['1', '2', '3'])
type(a_tuple)
```

Output:

```python
<class 'tuple'>
```

This example demonstrates how to convert or cast a Python list into a tuple.

## 2. Working With Tuples

There are not many ways to work with tuples due to the fact that they are immutable.
If you were to run `dir(tuple())`, you would find that tuples have only two methods:

* `count()`
* `index()`

You can use `count()` to find out how many elements match the value that you pass in:

```python
a_tuple = (1, 2, 3, 3)
a_tuple.count(3)
```

Output:

```python
2
```

In this case, you can find out how many times the integer `3` appears in the tuple.

You can use `index()` to find the first index of a value:

```python
a_tuple = (1, 2, 3, 3)
a_tuple.index(2)
```

Output:

```python
1
```

This example shows you that the number `2` is at index `1`, which is the second item in the tuple. Tuples are zero-indexed, meaning that the first element starts at zero.

Let’s try to modify an element in your tuple:

```python
a_tuple[0] = 8
```

Output:

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

Here you try to set the first element in the tuple to `8`. However, this causes a `TypeError` to be raised because tuples are immutable and cannot be changed.

## 3. Concatenating Tuples

Tuples can be joined together, which in programming is called “concatenation”. However, when you do that, you will end up creating a new tuple:

```python
a_tuple = (1, 2, 3, 3)
id(a_tuple)
```

Output:

```python
140617302751760
```

```python
a_tuple += (6, 7)
id(a_tuple)
```

Output:

```python
140617282270944
```

Here you concatenate a second tuple to the first tuple. You can use Python’s `id()` function to see that the variable, `a_tuple`, has changed. The `id()` function returns the id of the object. An object’s ID is equivalent to an address in memory. The ID number changed after concatenating the second tuple. That means that you have created a new object.

## 4. Special Case Tuples

There are two special-case tuples: a tuple with zero items and a tuple with one item. The reason they are special cases is that the syntax to create them is a little different.

### Empty Tuple

To create an empty tuple, you can do one of the following:

```python
empty = tuple()
len(empty)
type(empty)
```

Output:

```python
0
<class 'tuple'>
```

```python
also_empty = ()
len(also_empty)
```

Output:

```python
0
```

You can create an empty tuple by calling the `tuple()` function with no arguments or via assignment when using an empty pair of parentheses.

### Tuple with One Item

Now let’s create a tuple with a single element:

```python
single = 2,
len(single)
type(single)
```

Output:

```python
1
<class 'tuple'>
```

To create a tuple with a single element, you can assign a value with a following comma. While the parentheses are usually optional, I highly recommend them for single-item tuples as the comma can be easy to miss.

## Wrapping Up

In this chapter, you learned how to create a tuple in three different ways. You also learned that tuples are immutable. Finally, you learned how to concatenate tuples and create empty tuples.

You learned the following in this chapter:

* Create tuples
* Work with tuples
* Concatenate tuples
* Special case tuples
```
