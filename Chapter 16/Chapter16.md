Classes are an important concept in object-oriented programming (OOP). They allow us to create our own data types that can have properties (variables) and behaviors (functions).

---

## Classes**

### 1. **What is a Class?**

A **class** is a blueprint for creating objects.
Objects are instances of classes.
Think of a class like a **template**, and the object is a **real thing** created from that template.

Example:

* **Class**: Car (defines what a car is and what it can do).
* **Object**: My car (an actual car created from the Car class).

---

### 2. **Creating a Class**

To define a class, we use the `class` keyword. Here’s an example:

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def drive(self):
        print(f"The {self.make} {self.model} is driving!")
```

* `__init__(self, make, model)` is the **constructor**. It runs when we create an object of the class. It sets the initial values for the object.
* `self` refers to the **instance** of the class (the actual object we create).
* `drive()` is a **method** of the class. It represents the action that can be done by the object.

---

### 3. **Creating an Object from the Class**

Now, let's create an object of the `Car` class:

```python
my_car = Car("Toyota", "Corolla")
```

* `my_car` is an **object** (an instance) of the `Car` class.
* We pass `"Toyota"` and `"Corolla"` to the `__init__` method, which sets the `make` and `model` properties.

---

### 4. **Accessing Properties and Methods**

We can **access** the properties and **call** the methods using the object:

```python
print(my_car.make)    # Output: Toyota
print(my_car.model)   # Output: Corolla

my_car.drive()        # Output: The Toyota Corolla is driving!
```

* `my_car.make` and `my_car.model` access the properties.
* `my_car.drive()` calls the method to make the car "drive".

---

### 5. **Multiple Objects**

We can create multiple objects from the same class:

```python
car1 = Car("BMW", "X5")
car2 = Car("Audi", "A4")

car1.drive()  # Output: The BMW X5 is driving!
car2.drive()  # Output: The Audi A4 is driving!
```

Each object has its own **properties** and can call the class’s **methods**.

---

### 6. **Inheritance**

**Inheritance** allows one class to **inherit** properties and methods from another class.

Example:

```python
class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)  # Call the parent class constructor
        self.battery_size = battery_size
    
    def charge(self):
        print(f"The {self.make} {self.model} is charging!")
```

* `ElectricCar` inherits from the `Car` class.
* `super().__init__(make, model)` calls the constructor of the parent class (`Car`) to set `make` and `model`.

Now you can create objects of `ElectricCar`:

```python
electric_car = ElectricCar("Tesla", "Model S", 100)
electric_car.drive()    # Output: The Tesla Model S is driving!
electric_car.charge()   # Output: The Tesla Model S is charging!
```

---
