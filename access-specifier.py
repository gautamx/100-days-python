# Access specifiers modifiers in python programming are used to limit the access of 
# class variables and class methods outside of class while implementing the concepts of inheritance.

# Types
    # Public access modifier
    # Private access modifier
    # Protected access modifier

####################################################################################################
# Public access specifier
####################################################################################################
# All the variables and methods (member functions) in python are by default public. 
# Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

a = Student('SS',23)
print(a.name,a.age)

####################################################################################################
# Private access specifier
####################################################################################################

# Private members of a class (variables or methods) are those members which are only accessible inside the class. 
# We cannot use private members outside of class.

# no strict concept of "private" access modifiers
# a convention has been established to indicate that a variable or method should be considered private
# double underscore (__) known as a "weak internal use indicator"

class Student: 
    def __init__(self, age, name): 
        self.__age = age        # An indication of private variable
        self.__name = name

    def get_age(self):
        return self.__age

    def __funName(self):        # An indication of private function
        self.y = 34
        print(self.y)

class Subject(Student):
    pass

b = Student(21,"Harry")
c = Subject(22,'Ron')

# calling by object of class Student
print(b._Student__age)          # private members can be accessed using mangled names
print(b.get_age())              # access using public functions
try:
    print(b.__age)              # throws error
except AttributeError as a:
    print(a)
try:
    print(b.__funName())        # throws error
except AttributeError as a:
    print(a)

# calling by object  of class Subject
try:
    print(c.__age)             # throws error
except AttributeError as a:
    print(a)
try:
    print(c.__funName())       # throws error
except AttributeError as a:
    print(a)
    
# Private members of a class cannot be accessed or inherited outside of class. 
# If we try to access or to inherit the properties of private members to child class (derived class). Then it will show the error.



#####################################################################################################################################
# Name mangling
#####################################################################################################################################
# Name mangling in Python is a technique used to protect class-private and superclass-private attributes 
# from being accidentally overwritten by subclasses.
class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"

my_object = MyClass()

print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
try:
    print(my_object.__mangled_attribute) # Throws an AttributeError
except AttributeError as a:
    print(a)
print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute



###############################################################################################################################
# Protected access specifier
###############################################################################################################################
# the term "protected" is used to describe a member (i.e., a method or attribute) of a class that is intended to be accessed 
# only by the class itself and its subclasses.
# single underscore is just a naming convention, and does not actually provide any protection or restrict access to the member
class Company:
    def __init__(self):
        self._name = 'Weyland-Yutani'

    def _weapon(self):
        print('xenomorph')

class Employee(Company):
    pass

x = Company()
y = Employee()

# calling by object of Company class
print(x._name)
x._weapon()

# calling by object of Employee class
print(y._name)
y._weapon()