# A class method is a type of method that is bound to the class and not the instance of the class. 
# In other words, it operates on the class as a whole, rather than on a specific instance of the class. 
# Class methods are defined using the "@classmethod" decorator, followed by a function definition. 
# The first argument of the function is always "cls," which represents the class itself.

# In Python, there are three main types of methods you can define within a class:
    # Instance methods
    # Class methods
    # Static methods

# Instance Methods
# These are the most common methods. They operate on an instance of the class and can access and modify the instance's attributes. 
# They take self as their first parameter.
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    # Instance method
    def display_info(self):
        return f"{self.make} {self.model}"

my_car = Car("Toyota", "Corolla")
print(my_car.display_info())  # Output: Toyota Corolla

# Class Methods
# Class methods operate on the class itself rather than instances. 
# They're defined using the @classmethod decorator and take cls (the class) as their first parameter.
class Employee:
    company = 'Apple'
    
    def show(self):
        print(f'The name is {self.name} and company is {self.company}.')

    @classmethod 
    def changeCompany(cls, newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = 'Avinash'
e1.show()
print(Employee.company)
# print(e1.company)

e1.changeCompany('Google')
e1.show()
print(Employee.company)

Employee.changeCompany('Meta')
e1.show()
print(Employee.company)

# another example
class Car:
    num_cars = 0
    
    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.num_cars += 1       # incremented everytime init is invoked, i.e., instance is created
    
    # Class method
    @classmethod
    def total_cars(cls):
        return f"Total cars created: {cls.num_cars}"

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
print(Car.total_cars())  # Output: Total cars created: 2
car2 = Car("Honda", "Brio")
print(Car.total_cars())  # Output: Total cars created: 3


# Static Methods
# Static methods don't operate on either instance or class. 
# They're defined using the @staticmethod decorator and don't take self or cls parameters.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    # Static method
    @staticmethod
    def is_vintage(year):
        return year < 1980      # related but not dependent on class or instance

car = Car("Ford", "Mustang", 1965)
print(Car.is_vintage(car.year))  # Output: True


# Instance methods: When you need to access or modify the instance's state
# Class methods: When you need to access or modify the class's state, or for alternative constructors
# Static methods: When you need a utility function related to the class but not dependent on instance or class state