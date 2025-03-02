# In case of multiple inheritance, Python follows a method resolution order (MRO) 
# to resolve conflicts between methods or attributes from different parent classes. 
# The MRO determines the order in which parent classes are searched for attributes and methods.

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
  
    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
    def __init__(self, dance, name):
        Employee.__init__(self, name, id = 29)
        Dancer.__init__(self, dance)

    def show(self):
        Employee.show(self)
        Dancer.show(self)

    def __call__(self):
        print('This is the call.')

o  = DancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
o.show()
o()
print(DancerEmployee.mro())