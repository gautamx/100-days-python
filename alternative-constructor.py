# In object-oriented programming, the term "constructor" refers to a special type of method that is automatically executed when an object is created from a class. 
# The purpose of a constructor is to initialize the object's attributes, allowing the object to be fully functional and ready to use.

# For example, consider a class named "Person" that has two attributes: "name" and "age". The default constructor for the class might look like this:
# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
# p = Person("John", "Doe")  # Standard construction

# However, you might want different ways to initialize your object. 
# Class methods can serve as alternative constructors:
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_full_name(cls,full_name):
        first_name, last_name = full_name.split()
        return cls(first_name, last_name)
    
p1 = Person('John', 'Doe')
print(p1.first_name, p1.last_name)

p2 = Person.from_full_name('Jane Smith')
print(p2.first_name, p2.last_name)


# Creating objects from different data formats
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        import re
        year, month, day = map( int, re.split("/|-", date_string) )     # multiple delimiters
        return cls(year,month,day)

    @classmethod
    def from_timestamp(cls, timestamp):
        import datetime
        date = datetime.datetime.fromtimestamp(timestamp)
        return cls(date.year, date.month, date.day)
    
d1 = Date(2025,2,27)
print(f'{d1.day}-{d1.month:02d}-{d1.year}')

d2 = Date.from_string("2025/02/27")
print(f'{d2.day}-{d2.month:02d}-{d2.year}')

d3 = Date.from_string("2025-02-28")
print(f'{d3.day}-{d3.month:02d}-{d3.year}')

d4 = Date.from_timestamp(1576278900)
print((f'{d4.day}-{d4.month:02d}-{d4.year}'))


# another example
class Database:
    def __init__(self, host, port, username, password, db_name):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.db_name = db_name
        # Connect to DB...
    
    @classmethod
    def development(cls):
        return cls("localhost", 5432, "dev_user", "dev_password", "dev_db")
    
    @classmethod
    def production(cls):
        return cls("prod.example.com", 5432, "prod_user", "secure_password", "prod_db")
    
    @classmethod
    def testing(cls):
        return cls("localhost", 5432, "test_user", "test_password", "test_db")

# Easy creation of different DB configurations
dev_db = Database.development()
prod_db = Database.production() 
test_db = Database.testing()