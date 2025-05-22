---

## **Functions** 

### 1. What is a **function**?

A **function** is a block of code.
It does a **job**, and you can **use it many times**.

Think of it like a **machine**:
You give it something (input), it gives you something back (output).

---

### 2. How to write a function

```python
def say_hello():
    print("Hello!")
```

This function is called `say_hello`.

To **use** the function:

```python
say_hello()
```

Output:

```
Hello!
```

---

### 3. Functions with **parameters** (input)

```python
def say_hello(name):
    print("Hello", name)
```

Call the function:

```python
say_hello("Ali")
```

Output:

```
Hello Ali
```

---

### 4. Functions with **return value**

A function can **give a result back**.

```python
def add(a, b):
    return a + b
```

Use it like this:

```python
result = add(3, 5)
print(result)
```

Output:

```
8
```

---

### 5. **Default value**

If no value is given, use a **default**:

```python
def say_hello(name="Guest"):
    print("Hello", name)
```

```python
say_hello()        # uses "Guest"
say_hello("Ayşe")  # uses "Ayşe"
```

Output:

```
Hello Guest
Hello Ayşe
```

---

### 6. Return **multiple values**

```python
def math(a, b):
    total = a + b
    product = a * b
    return total, product
```

```python
t, p = math(2, 3)
print(t)  # 5
print(p)  # 6
```

---
