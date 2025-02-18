# Sets are unordered collection of data items. They store multiple items in a single variable. 
# Set items are separated by commas and enclosed within curly brackets {}. 
# Sets are unchangeable, meaning you cannot change items of the set once created. 
# Sets do not contain duplicate items.
info = {"Carla", 19, False, 5.9, 19, 19, 0}     # false and zero are considered same in set
# info = set(("Carla", 19, False, 5.9, 19, 19, 0))      # using a set constructor
print(info)
print(type(info))
# items of set occur in random order and hence they cannot be accessed using index numbers
empty_set = {}
print(type(empty_set))      # type --> dict

q = set()           # explicitly empty set definition    
print(type(q))      # type --> set

# You can access items of set using a for loop
for i in info:
    print(i, end=' ')