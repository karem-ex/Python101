# python_lists.py

# 1. Creating Lists

# Creating a list using square brackets
my_list = [1, 2, 3]
print("List created with square brackets:", my_list)

# Creating a list using list()
list_of_strings = list('abc')
print("List created using list():", list_of_strings)

# Creating an empty list
empty_list = []
print("Empty list:", empty_list)

# Creating an empty list using list()
another_empty_list = list()
print("Another empty list using list():", another_empty_list)

# 2. List Methods

# Creating a sample list
my_list = ['a', 'b', 'c', 'c']
print("\nInitial list:", my_list)

# Using append() to add an item at the end
my_list.append(1)
print("After append:", my_list)

# Using insert() to add an item at a specific position
my_list.insert(0, 'first')
print("After insert:", my_list)

# Using extend() to add another list's items
other_list = [4, 5, 6]
my_list.extend(other_list)
print("After extend:", my_list)

# Using count() to count occurrences of an item
print("Count of 'c':", my_list.count('c'))

# Using reverse() to reverse the list
my_list.reverse()
print("After reverse:", my_list)

# 3. Accessing and Changing List Elements

# Accessing items by index
print("\nAccessing items by index:")
print("Item at index 0:", my_list[0])
print("Item at index 2:", my_list[2])

# Using negative indexing
print("Last item using negative index:", my_list[-1])

# 4. Deleting From a List

# Using clear() to remove all items
my_list.clear()
print("\nAfter clear():", my_list)

# Re-creating the list
my_list = [7, 8, 9]
print("Re-created list:", my_list)

# Using pop() to remove the last item
removed_item = my_list.pop()
print("Removed item using pop():", removed_item)
print("List after pop():", my_list)

# Using remove() to remove a specific item
my_list.remove(8)
print("List after remove(8):", my_list)

# Using del to delete an item by index
del my_list[1]
print("List after del my_list[1]:", my_list)

# 5. Sorting a List

# Creating a sample list
my_list = [4, 10, 2, 1, 23, 9]

# Using sort() to sort the list in place
my_list.sort()
print("\nSorted list using sort():", my_list)

# Using sorted() to get a sorted list (without modifying the original list)
sorted_list = sorted(my_list)
print("Sorted list using sorted():", sorted_list)

# 6. List Slicing

# Slicing the list
print("\nList slicing:")
print("Slicing from index 1 to 3:", my_list[1:3])

# Using negative indexing in slicing
print("Slicing from second to last item:", my_list[-2:])

# Slicing up to a specific index
print("Slicing up to index 3:", my_list[:3])

# 7. Copying a List

# Creating a sample list
my_list = [1, 2, 3]

# Using copy() to create a shallow copy
new_list = my_list.copy()
print("\nNew list created using copy():", new_list)

# Using slicing to create a copy
new_list_slice = my_list[:]
print("New list created using slicing:", new_list_slice)
