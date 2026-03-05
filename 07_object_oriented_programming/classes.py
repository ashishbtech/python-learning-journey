# classes.py

# Define a simple class
class Person:
    # Constructor method (__init__) initializes object attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method inside the class
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create objects (instances) of the class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Call methods on objects
person1.greet()
person2.greet()