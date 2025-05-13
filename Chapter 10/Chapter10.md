# Python Learning About Loops


### 1. **Create a For Loop**

The `for` loop is used to iterate over a collection (like a list, string, etc.). It repeats a block of code for each item in the collection.

**Example:**

```python
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
```

This loop will print each number in the list.

---

### 2. **Loop Over a String**

You can also loop through each character of a string using a `for` loop.

**Example:**

```python
word = "Python"
for char in word:
    print(char)
```

This will print each character of the word "Python" one by one.

---

### 3. **Loop Over a Dictionary**

A **dictionary** consists of key-value pairs. You can loop through both keys and values in a dictionary using the `for` loop.

**Example:**

```python
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Loop through keys and values
for key, value in person.items():
    print(f"{key}: {value}")
```

This will print each key-value pair in the dictionary.

---

### 4. **Extract Multiple Values from a Tuple**

A **tuple** is an ordered collection of elements. If you have a tuple, you can extract multiple values at once while looping through it.

**Example:**

```python
people = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

# Extracting multiple values from each tuple (name and age)
for name, age in people:
    print(f"Name: {name}, Age: {age}")
```

Here, we extract both the name and the age from each tuple and print them.

---

### 5. **Use Enumerate with Loops**

The `enumerate()` function allows you to loop through a collection and get both the index and the value of each item. This is useful when you need to know the position of an item in the collection.

**Example:**

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

In this example, the loop prints both the index and the value (fruit) from the list.

---

### 6. **Create a While Loop**

A `while` loop runs as long as a condition is true. Once the condition becomes false, the loop stops.

**Example:**

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

This will print the numbers from 0 to 4. The loop continues until `count` is no longer less than 5.

---

### 7. **Breakout of a Loop**

The `break` statement is used to exit a loop before it naturally finishes. When the `break` statement is encountered, the loop is immediately terminated.

**Example:**

```python
for i in range(10):
    if i == 5:
        break  # Exit the loop when i equals 5
    print(i)
```

This loop will print numbers from 0 to 4, and when `i` reaches 5, the `break` statement will exit the loop.

---

### 8. **Use Continue**

The `continue` statement is used to skip the current iteration of the loop and move to the next one.

**Example:**

```python
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
```

In this case, only the odd numbers from 0 to 9 will be printed because even numbers are skipped using `continue`.

---

### 9. **Use Else with Loops**

In Python, you can use the `else` block with loops. The `else` block will run if the loop completes without hitting a `break` statement. If the loop is interrupted by `break`, the `else` block won't run.

**Example:**

```python
for i in range(5):
    print(i)
else:
    print("Loop completed!")
```

Here, the loop will print numbers from 0 to 4, and once the loop finishes, `"Loop completed!"` will be printed.

---

### 10. **Nest Loops**

You can nest one loop inside another loop. This is useful when you're working with multi-dimensional data (like lists of lists, matrices, etc.).

**Example:**

```python
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
```

In this example, the outer loop runs 3 times, and the inner loop runs 2 times for each outer loop iteration, printing a total of 6 outputs.

---

