# Operator Overloading is a feature in Python that allows developers to redefine the behavior of mathematical and comparison operators 
# for custom data types. This means that you can use the standard mathematical operators (+, -, *, /, etc.) and 
# comparison operators (>, <, ==, etc.) in your own classes, just as you would for built-in data types like int, float, and str.

# we overload an operator in Python by defining special dunder methods in class

try:
    p1 = (1,2)  # point on a 2d plane
    p2 = (3,4)
    p3 = p1 + p2
    print(p3)
except NameError as n:
    print(n)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
p1 = Point(1,2)
p2 = Point(3,4)
p3 = p1 + p2
print(type(p3))
print(p3.x, p3.y)

# operator overloading is not limited to the built-in operators, you can overload any user-defined operator as well

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):      # operator overloading
        return f'{self.i}i + {self.j}j + {self.k}k'          # object of this class will give this format for print(obj)

    def __add__(self,x):    # operator overloading
        return Vector(self.i+x.i, self.j+x.j, self.k+x.k)   # this is how objects of this class will be added
    
v1 = Vector(1,2,3)
print(type(v1))
print(v1)

v2 = Vector(4,5,6)
print(type(v2))
print(v2)

v3 = v1 + v2
print(type(v3))
print(v3)