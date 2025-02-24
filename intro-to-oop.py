# In programming languages, mainly there are two approaches that are used to write program or code.
# 1) Procedural Programming
# 2) Object-Oriented Programming

# The basic idea of object-oriented programming (OOP) in Python
# is to use classes and objects to represent real-world concepts and entities.

# A class is a blueprint or template for creating objects. It defines the properties and methods that an object of that class will have. 
# Properties are the data or state of an object, and methods are the actions or behaviors that an object can perform.

# An object is an instance of a class, and it contains its own data and methods. 
# For example, you could create a class called "Person" that has properties such as name and age, and methods such as speak() and walk(). 
# Each instance of the Person class would be a unique object with its own name and age, but they would all have the same methods to speak and walk.

# Encapsulation

# One of the key features of OOP in Python is encapsulation, 
# which means that the internal state of an object is hidden and can only be accessed or modified through the object's methods. 
# This helps to protect the object's data and prevent it from being modified in unexpected ways.

# Inheritance

# Another key feature of OOP in Python is inheritance, 
# which allows new classes to be created that inherit the properties and methods of an existing class. 
# This allows for code reuse and makes it easy to create new classes that have similar functionality to existing classes.

# Polymorphism

# Polymorphism is also supported in Python, which means that objects of different classes can be treated as if they were objects of a common class. 
# This allows for greater flexibility in code and makes it easier to write code that can work with multiple types of objects.

# OOP in Python allows developers to model real-world concepts and entities using classes and objects, 
# encapsulate data, reuse code through inheritance, and write more flexible code through polymorphism.


###################################################################################################################################################
###################################################################################################################################################

# class --> template for creating objects
# provide initial value to variables (attributes)
# define functions (methods)
# Object --> instance of the class used to access the properties of the class

# create a class
class Person:
    name = 'MK'
    age = 27

    # SELF PARAMETER is a reference to the current instance of the class, and is used to access variables that belongs to the class.
    # It must be provided as the extra parameter inside the method definition --> desc(self)
    def desc(self):
        print(f'My name is {self.name}. I am {self.age}.')

# user-defined objects are created using the class keyword
a = Person()
b = Person()

b.name = 'SS'
b.age = 29

# a attributes will have default/initial values
# b attributes will have updated values
a.desc()
b.desc()


######################################################################################################################################
# CONSTRUCTOR
# A constructor is a special method in a class used to create and initialize an object of a class. 
# There are different types of constructors. 
# A constructor is a unique function that gets called automatically when an object is created of a class. 
# The main purpose of a constructor is to initialize or assign values to the data members of that class. 
# It cannot return any value other than None.
class animals:
    # init is one of the reserved functions in Python. In OOP, it is known as a constructor.
    # When the constructor accepts arguments along with self, it is known as parameterized constructor. Otherwise, default constructor.
    def __init__(self, animal, group):
        self.animal = animal            # passed arguments assigned to attributes
        self.group = group

a = animals('lion','mammal')            # passed arguments
b = animals('crab','crustacean')

print(a.animal,a.group)
print(b.animal,b.group)


class dummy:
    # When the constructor doesn't accept any arguments from the object 
    # and has only one argument, self, in the constructor, it is known as a default constructor.
    def __init__(self):
        print('This is a default contructor')
    # don't have to pass args while creating objects
obj1 = dummy()      # prints the statement in constructor


# example
class Person:

    def __init__(self, name, occ):
        # print('I am alive...')
        self.name = name
        self.occ = occ

    def info(self):
        print(f'I am {self.name} and I am a {self.occ}')

a = Person('MK','Teacher')
b = Person('SS','Analyst')

a.info()
b.info()

a.name = 'Mo'
print(a.name)
a.occ = '<3'
a.info()