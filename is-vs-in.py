# In Python, is and == are both comparison operators that can be used to check if two values are equal.

# The 'is' operator compares the identity of two objects
# the == operator compares the values of the objects

# 'is' will return True if the objects being compared are the exact same object in memory, 
# while == will return True if the objects have the same value.

a = [1,2,3]
b = [1,2,3]

print(a == b)   # True
print(a is b)   # False
# a and b are two separate lists that have the same values
# a and b are not the same object in memory

# strings and integers are immutable
# for strings and integers, is and == will always return the same result

a = "hello"
b = "hello"

print(a == b)  # True
print(a is b)  # True

a = 5
b = 5

print(a == b)  # True
print(a is b)  # True
# a and b are both pointing to the same object in memory

# For mutable objects such as lists and dictionaries, 'is' and == can behave differently. 

# In general, you should use == when you want to compare the values of two objects, 
# and use 'is' when you want to check if two objects are the same object in memory.

a = None
b = None

print(a is b)       # exact location of object in memory
print(a is None)    # exact location of object in memory
print(a == b)       # value