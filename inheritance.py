# When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. 
# In addition, it can have its own properties and methods,this is called as inheritance.

# class Parent:
#   Body of base class
# class Child(Parent):
#   Body of derived class

# Types:
    # Single inheritance
    # Multiple inheritance
    # Multilevel inheritance
    # Hierarchical Inheritance
    # Hybrid Inheritance

######################################################################
# Single inheritance --> single parent class
class Parent:
    def func1(self):
        print('This function is in Parent class.')

class Child(Parent):
    def func2(self):
        print('This function is in Child class.')

obj1 = Child()
obj1.func2()
obj1.func1()

#######################################################################
# Multiple inheritance --> multiple parent class
class dummy:
    def func3(self):
        print('This is a dummy class.')

class Infant(Child, dummy):        # Child already inherits from Parent --> multi-level
    def func4(self):
        print('This function is in class with multiple parents.')

obj2 = Infant()
obj2.func4()
obj2.func3()
obj2.func2()
obj2.func1()


##########################################################################
# Multi-level inheritance
class Grandfather:
    def __init__(self, Grandfathername):
        self.Grandfathername = Grandfathername

class Father(Grandfather):
    def __init__(self, Fathername, Grandfathername):
        self.Fathername = Fathername
        Grandfather.__init__(self, Grandfathername)

class Son:
    def __init__(self, Sonname, Fathername, Grandfathername):
        self.Sonname = Sonname
        Father.__init__(self, Fathername, Grandfathername)

    def print_name(self):
        print(f'Son: {obj3.Sonname}\nFather: {obj3.Fathername}\nGrandfather: {obj3.Grandfathername}')

obj3 = Son('Gautam','Rameshchandra','Kantilal')
obj3.print_name()


#########################################################################################
# hierarchical inheritance --> more than one derived class are created from a single base
class Super:
    def func10(self):
        print("This function is in Super class.")

class Sub1(Super):
    def func11(self):
        print("This function is in Sub1 class.")
      
class Sub2(Super):
    def func12(self):
        print("This function is in Sub2 class.")
 
obj10 = Sub1()
obj20 = Sub2()

obj20.func10()
# obj20.func11()      # throws error
obj20.func12()

# Inheritance consisting of multiple types of inheritance is called hybrid inheritance.