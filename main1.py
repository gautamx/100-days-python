# this is a 
# multi-line comment 

# print statement arguments
print("Hello","World",sep="~",end="!\n")

# data types
a = 1
print(type(a))
a1 = 1.12345
print(type(a1))
a2 = complex(1,2)
print(type(a2))
b = "1"
print(type(b))
c = None
print(type(c))
d = False
print(type(d))

# we cannot operate on two different types of data

mouse=9
cat1=mouse
cat2="mouse"
print(cat1,cat2)

# int float complex string boolean list tuple dict

# list is mutable
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

# tuple is immutable
tuple1 = (8, 2.3, ("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

# dict key:value
dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)

# in python, everything is an object