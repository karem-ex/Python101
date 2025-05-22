---

###  What is "Working with Files"?

Sometimes we want to **read from** or **write to** a file (like a `.txt` file).
For example: reading a diary, writing notes, saving data, etc.

---

### 3 Main Steps

1. **Open the file**
2. **Read or write**
3. **Close the file**

But in Python, we usually use the `with` keyword so Python closes the file **automatically**.

---

### Reading a File

```python
with open("myfile.txt", "r") as file:
    content = file.read()
    print(content)
```

* `"r"` means **read** mode.

Other read options:

```python
file.readline()    # reads one line
file.readlines()   # reads all lines in a list
```

---

### Writing to a File

```python
with open("myfile.txt", "w") as file:
    file.write("Hello!\n")
```

* `"w"` means **write** mode.
* It **removes old content** and writes new content.

---

### Adding to a File

```python
with open("myfile.txt", "a") as file:
    file.write("This is a new line.\n")
```

* `"a"` means **append** mode.
* It **keeps old content** and adds new content to the end.

---

### Simple Practice

Try this code:

```python
# Write a line
with open("notes.txt", "w") as f:
    f.write("I am learning Python.\n")

# Add a new line
with open("notes.txt", "a") as f:
    f.write("Today I studied file handling.\n")

# Read all lines
with open("notes.txt", "r") as f:
    print(f.read())
```

---

