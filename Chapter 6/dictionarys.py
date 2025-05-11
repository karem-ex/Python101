# Creating a simple dictionary
student = {
    'name': 'Ali',
    'age': 20,
    'course': 'Computer Science'
}

print(student)


# Creating a dictionary using dict() method
person = dict(name='John', age=30, city='New York')
print(person)


student = {'name': 'Ali', 'age': 20, 'course': 'Computer Science'}
print(student['name'])  # 'Ali'


student = {'name': 'Ali', 'age': 20, 'course': 'Computer Science'}
print(student.get('age'))  # 20
print(student.get('address'))  # None


student = {'name': 'Ali', 'age': 20, 'course': 'Computer Science'}
student['age'] = 21  # Updating age
print(student)


student = {'name': 'Ali', 'age': 20, 'course': 'Computer Science'}
student['address'] = 'Istanbul'  # Adding new key-value pair
print(student)


student = {'name': 'Ali', 'age': 20, 'course': 'Computer Science'}
del student['course']  # Deleting the 'course' key
print(student)


student = {'name': 'Ali', 'age': 20, 'course': 'Computer Science'}
course = student.pop('course')  # Removing and returning the 'course' value
print(course)  # 'Computer Science'
print(student)


student = {'name': 'Ali', 'age': 20, 'course': 'Computer Science'}
student.clear()  # Clears all items
print(student)


student = {'name': 'Ali', 'age': 20, 'course': 'Computer Science'}
print(student.keys())  # dict_keys(['name', 'age', 'course'])


print(student.values())  # dict_values(['Ali', 20, 'Computer Science'])


# dict_items([('name', 'Ali'), ('age', 20), ('course', 'Computer Science')])
print(student.items())
