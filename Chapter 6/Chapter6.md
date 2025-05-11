# Python Dictionary

A dictionary is a (key, value) pair. 

Starting in Python 3.7, dictionaries are ordered. What that means is that when you add a new (key, value) pair to a dictionary, it remembers what order they were added. Prior to Python 3.7, this was not the case and you could not rely on insertion order.

You will learn how to do the following in this chapter:
- Creating dictionaries
- Accessing dictionaries
- Dictionary methods
- Modifying dictionaries
- Deleting items from your dictionary


## 1. Creating Dictionaries

You can create a dictionary in a couple of different ways. The most common method is by placing a comma-separated list of key: value pairs within curly braces.

Let’s look at an example:

```python
sample_dict = {'first_name': 'James', 'last_name': 'Doe', 'email': 'jdoe@gmail.com'}
sample_dict
````

Output:

```python
{'first_name': 'James', 'last_name': 'Doe', 'email': 'jdoe@gmail.com'}
```

You can also use Python’s built-in `dict()` function to create a dictionary. `dict()` will accept a series of keyword arguments (i.e. `one='one'`, `two='two'`, etc), a list of tuples, or another dictionary.

Here are a couple of examples:

```python
numbers = dict(one=1, two=2, three=3)
numbers
```

Output:

```python
{'one': 1, 'two': 2, 'three': 3}
```

```python
info_list = [('first_name', 'James'), ('last_name', 'Doe'), ('email', 'jdoes@gmail.com')]
info_dict = dict(info_list)
info_dict
```

Output:

```python
{'first_name': 'James', 'last_name': 'Doe', 'email': 'jdoes@gmail.com'}
```

## 2. Accessing Dictionaries

Dictionaries’ claim to fame is that they are very fast. You can access any value in a dictionary via the key. If the key is not found, you will receive a `KeyError`.

Let’s take a look at how to use a dictionary:

```python
sample_dict = {'first_name': 'James', 'last_name': 'Doe', 'email': 'jdoe@gmail.com'}
sample_dict['first_name']
```

Output:

```python
'James'
```

To get the value of `first_name`, you must use the following syntax: `dictionary_name[key]`.

Now let’s try to get a key that doesn’t exist:

```python
sample_dict['address']
```

Output:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'address'
```

You can use Python’s `in` keyword to ask if a key is in the dictionary:

```python
'address' in sample_dict
```

Output:

```python
False
```

```python
'first_name' in sample_dict
```

Output:

```python
True
```

You can also check to see if a key is **not** in a dictionary by using Python’s `not` keyword:

```python
'first_name' not in sample_dict
```

Output:

```python
False
```

```python
'address' not in sample_dict
```

Output:

```python
True
```


### 3. **Dictionary Methods**

Dictionaries in Python have special functions called "methods" that you can use to work with them.

Here are some common dictionary methods:

* **`get(key)`**: This method is used to get the value of a key. If the key doesn't exist, it returns `None` (or a default value if you provide one).

  ```python
  my_dict = {'name': 'John', 'age': 25}
  print(my_dict.get('name'))  # Output: John
  print(my_dict.get('city', 'Unknown'))  # Output: Unknown
  ```

* **`keys()`**: This method returns all the keys in the dictionary.

  ```python
  print(my_dict.keys())  # Output: dict_keys(['name', 'age'])
  ```

* **`values()`**: This method returns all the values in the dictionary.

  ```python
  print(my_dict.values())  # Output: dict_values(['John', 25])
  ```

* **`items()`**: This method returns a list of tuples, where each tuple is a key-value pair.

  ```python
  print(my_dict.items())  # Output: dict_items([('name', 'John'), ('age', 25)])
  ```

* **`update(other_dict)`**: This method is used to add the items from another dictionary to your dictionary.

  ```python
  my_dict.update({'city': 'New York'})
  print(my_dict)  # Output: {'name': 'John', 'age': 25, 'city': 'New York'}
  ```

---

### 4. **Modifying Dictionaries**

You can change the contents of a dictionary by modifying its values or adding new key-value pairs.

* **Changing a value**: You can change the value of an existing key.

  ```python
  my_dict = {'name': 'John', 'age': 25}
  my_dict['age'] = 30  # Change the value of 'age'
  print(my_dict)  # Output: {'name': 'John', 'age': 30}
  ```

* **Adding a new key-value pair**: If the key doesn't exist, you can add a new pair.

  ```python
  my_dict['city'] = 'Los Angeles'
  print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'Los Angeles'}
  ```

---

### 5. **Deleting Items from Your Dictionary**

There are several ways to delete items from a dictionary.

* **`del` keyword**: You can use `del` to remove a key-value pair.

  ```python
  del my_dict['age']
  print(my_dict)  # Output: {'name': 'John', 'city': 'Los Angeles'}
  ```

* **`pop(key)`**: This method removes the item with the specified key and returns the value.

  ```python
  city = my_dict.pop('city')
  print(city)  # Output: Los Angeles
  print(my_dict)  # Output: {'name': 'John'}
  ```

* **`clear()`**: This method removes all items from the dictionary, making it empty.

  ```python
  my_dict.clear()
  print(my_dict)  # Output: {}
  ```

---

