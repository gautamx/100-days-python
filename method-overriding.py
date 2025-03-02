# Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method in a derived class. 
# The method in the derived class is said to override the method in the base class. 
# When you create an instance of the derived class and call the overridden method, 
# the version of the method in the derived class is executed, rather than the version in the base class.
import math

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        print('Calculating area...')
        return self.x * self.y

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius,radius)

    # method overriding
    def area(self):
        # can be useful when you want to extend the behavior of the base class method or replace it entirely.
        return math.pi * super().area()

obj1 = Shape(5,7)
print(obj1.area())

obj2 = Circle(7)
print(obj2.area())

# In this example, the Circle class inherits from the Shape class, and overrides the area method. 

# It's important to note that when you override a method, 
# the new implementation must have the same method signature as the original method. 
# This means that the number and type of arguments, as well as the return type, must be the same.