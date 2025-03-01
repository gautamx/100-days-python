# Dunder methods (short for "double underscore" methods) in Python are special methods surrounded by double underscores 
# that give you control over how Python objects behave in various situations. 
# They're also called "magic methods" or "special methods."

from emp import Employee

e1 = Employee("Shefali")

print(str(e1))
print(repr(e1))
print(e1.name)
print(len(e1))
e1()                    # __call__