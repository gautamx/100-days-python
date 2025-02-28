# The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object.
x = [1,2,3]
print(dir(x))

print('\n')
# The __dict__ attribute returns a dictionary representation of an object's attributes.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person('SS',29)
print(dir(p))
print('\n')
print(p.__dict__)


# The help() function is used to get help documentation for an object, including a description of its attributes and methods.
# print(help(str))
# >>help(str) in python console