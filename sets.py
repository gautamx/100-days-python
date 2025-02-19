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

empty_set = set()           # explicitly empty set definition    
print(type(empty_set))      # type --> set

# You can access items of set using a for loop
for i in info:
    print(i, end=' ')

print('\n')
#############################################################################################
# We can perform operations like union and intersection on the sets just like in mathematics.

# set.union() and set.update()
# union() method returns a new set whereas update() method adds item into the existing set from another set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)
print(cities)

cities.update(cities2)
print(cities)

# set.intersection() and set.intersection_update()
# The intersection() and intersection_update() methods prints only items that are similar to both the sets. 
# The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)
print(cities)

cities.intersection_update(cities2)
print(cities)

# set.symmetric_difference() and set.symmetric_difference_update()
# The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. 
# The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)
print(cities)

cities.symmetric_difference_update(cities2)
print(cities)

# set.difference() and set.difference_update()
# The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. 
# The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)
print(cities)

cities.difference_update(cities2)
print(cities)


#############################################################################
# set methods

# isdisjoint()
# checks if items of given set are present in another set. 
# This method returns False if items are present, else it returns True.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

# issuperset()
# checks if all the items of a particular set are present in the original set. 
# It returns True if all the items are present, else it returns False.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities3.issuperset(cities2))

# issubset()
# hecks if all the items of the original set are present in the particular set. 
# It returns True if all the items are present, else it returns False.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))

# add()
# add a single item to the set
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

# update()
# add more than one item, simply create another set 
# or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)