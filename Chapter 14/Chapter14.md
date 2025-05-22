---

### What is "Importing"?

Python has many **tools** (like math, random, datetime...).
These tools are in **modules**.
To use a module, we must **import** it.

---

### Example 1: Importing a Module

```python
import math

print(math.sqrt(16))  # → 4.0
```

* `math` is a **module**
* `math.sqrt()` gives square root

---

### Example 2: Import One Function

```python
from math import sqrt

print(sqrt(25))  # → 5.0
```

* We imported only `sqrt`, not all `math`

---

### Example 3: Import With Alias (short name)

```python
import math as m

print(m.sqrt(36))  # → 6.0
```

* `math` is now called `m`

---

### 🔍 Common Built-in Modules

| Module     | Use for...                 |
| ---------- | -------------------------- |
| `math`     | math functions             |
| `random`   | random numbers             |
| `datetime` | date and time              |
| `os`       | working with files/folders |
| `sys`      | system-related stuff       |

---

### Small Practice

Try this in your code:

```python
import random

number = random.randint(1, 10)
print("Random number:", number)
```

---

### Import Your Own File

You can also create your own `.py` file and import it!

**my\_utils.py**

```python
def hello():
    print("Hello from my_utils!")
```

**main.py**

```python
import my_utils

my_utils.hello()
```

---
