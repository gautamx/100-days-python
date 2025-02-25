# In Python, getters and setters are methods that allow you to control access to attributes (variables) of a class. 
# They're part of what's known as "property management" in object-oriented programming.

# Getters (or accessors): Methods that retrieve the value of a private attribute
# Setters (or mutators): Methods that modify the value of a private attribute

# Python provides a built-in @property decorator that makes implementing getters and setters elegant and Pythonic.

class Person:
    def __init__(self,name,age):
        self._name = name           # underscore indicates "private" by convention
        self._age = age

    def show(self):
        return self._age

    @property
    def name(self):
        """Getter for name"""
        return self._name
    
    @name.setter
    def name(self, value):
        """Setter for name"""
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value

    @property
    def age(self):
        """Getter for age"""
        return self._age
    
    @age.setter
    def age(self, value):
        """Setter for age"""
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

a = Person('MM',22)
print(a.name)
print(a.age)
a.name = 'MK'
a.age = 27          # accesses the value like an attribute
print(f'I am {a.name}. I am {a.age}.')

print(a.show())     # accesses the same value but like a method
# Both can return the same data, but properties are meant to provide attribute-like access to methods
# Methods typically perform an action, while properties typically represent a state

# Using validation
try:
    a.age = -5  # Raises ValueError
except ValueError as e:
    print(e)  # "Age cannot be negative"