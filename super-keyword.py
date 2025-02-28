# The super() keyword in Python is used to access methods and properties from a parent or superclass.

# basic usage
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

obj1 = Child('SS', 29)
print(obj1.name, obj1.age)


# usage with methods
class Animal:
    def speak(self):
        return 'some sound'
    
class Dog(Animal):
    def speak(self):
        parent_sound = super().speak()
        return f'{parent_sound} and then bark.'
    
obj2 = Dog()
print(obj2.speak())



# super() becomes particularly useful with multiple inheritance by following Python's Method Resolution Order (MRO)
class A:
    def method(self):
        print('A.method called')

class B(A):
    def method(self):
        print('B.method called')
        super().method()

class C(A):
    def method(self):
        print('C.method called')
        super().method()

class D(B, C):
    def method(self):
        print('D.method called')
        super().method()

obj3 = D()
obj3.method()
# Python follows the MRO (D → B → C → A) when resolving the super() calls.


# The shorthand super() in Python 3 is equivalent to super(CurrentClass, self). 
class Parent:
    def method(self):
        print("Parent method")
        
class Child(Parent):
    def method(self):
        print("Child method")
        super(Child, self).method()  # Explicitly reference the parent of Child
        
child = Child()
child.method()
# Output:
# Child method
# Parent method


# when you have multiple parent class, python follows method resolution order (MRO)
# When you call super().parent_method(), it calls the next class in the MRO after the current class
class ParentClass1:
    def parent_method(self):
        print("This is the parent method of ParentClass1.")

class ParentClass2:
    def parent_method(self):
        print("This is the parent method of ParentClass2.")

class ChildClass(ParentClass1, ParentClass2):       # class ChildClass(ParentClass2, ParentClass1): will change MRO
    def child_method(self):
        print("This is the child method.")
        super().parent_method()                 # calls ParentClass1's method
        ParentClass2.parent_method(self)        # calls ParentClass2's method

child_object = ChildClass()
child_object.child_method()

# check MRO
print(ChildClass.__mro__)

# if you want to call ParentClass2 method
ParentClass2.parent_method(child_object)  # Call explicitly