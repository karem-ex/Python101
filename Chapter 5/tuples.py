# 1.Create Tuple
my_tuple = (1, 2, 3, "Python", True)

print(my_tuple)

print(type(my_tuple))

# 2.Work with Tuples

my_tuple = (1, 2, 3, 3, 4)

# count() ile 3 sayısının kaç kez geçtiğini bulma
print(my_tuple.count(3))  # 2

# index() ile 2 sayısının index'ini bulma
print(my_tuple.index(2))  # 1


# 3.Concatenate Tuples

# First tuple
tuple1 = (1, 2, 3)

# Second tuple
tuple2 = (4, 5, 6)

# Concatenate Tuples
result = tuple1 + tuple2

print(result)


# 4.Special Case Tuples

# Create Empty Tuple
empty_tuple = ()

print(empty_tuple)

print(type(empty_tuple))


# Create One item in Tuple
single_element_tuple = (5,)

print(single_element_tuple)

print(type(single_element_tuple))
