# Class variables are defined at the class level and are shared among all instances of the class. 
# They are defined outside of any method and are usually used to store information that is common to all instances of the class.
class MyClass:
    class_var = 0

    def __init__(self):
        MyClass.class_var += 1      # not self.class_var b/c variable belongs to class not instance

    def print_class_var(self):
        print(MyClass.class_var)

obj1 = MyClass()            # class variable increments
obj1.print_class_var()
print(MyClass.class_var)

obj2 = MyClass()            # class variable increments again
obj2.print_class_var()
obj1.print_class_var()

print(MyClass.class_var)

print('\n')

# Instance variables are defined at the instance level and are unique to each instance of the class. 
# They are defined inside the init method and are usually used to store information that is specific to each instance of the class.
class MyClass2:
    instance_var = 0                # class variable remains zero
    
    def __init__(self):
        self.instance_var += 1      # variable belongs to instance
        # self.instance_var += 1

    def print_instance_var(self):
        print(self.instance_var)

obj3 = MyClass2()                   # instance variable increments, class variable zero
obj3.print_instance_var()
print(MyClass2.instance_var)

obj4 = MyClass2()                   # instance variable increments, class variable zero
obj4.print_instance_var()
obj3.print_instance_var()           # remains same

print(MyClass2.instance_var)        # class variable remains zero, instance variable increments


# In summary, class variables are shared among all instances of a class and are used to store information that is common to all instances. 
# Instance variables are unique to each instance of a class and are used to store information that is specific to each instance.

# in python, class variables are defined outside of any methods and don't need to be explicitly declared as class variable. 
# They are defined in the class level and can be accessed via classname.varibale_name or self.class.variable_name. 
# But instance variables are defined inside the methods and need to be explicitly declared as instance variable by using self.variable_name.


# another example
class Employee:
  companyName = "Apple"
  noOfEmployees = 0
  def __init__(self, name):
    self.name = name                # updating instance variable
    self.raise_amount = 0.02
    Employee.noOfEmployees +=1      # incrementing class variable
  def showDetails(self):
    print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

# Employee.showDetails(emp1)
emp1 = Employee("Harry")
emp1.raise_amount = 0.3
emp1.companyName = "Apple India"    # updating instance variable
emp1.showDetails()
print(Employee.companyName)
Employee.companyName = "Google"     # updating class variable
print(Employee.companyName)

emp2 = Employee("Rohan")
emp2.companyName = "Nestle"
emp2.showDetails()
print(Employee.companyName)
print(emp1.companyName)
print(emp2.companyName)
print(Employee.noOfEmployees)

emp3 = Employee("Hari")
emp3.showDetails()