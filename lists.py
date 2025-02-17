# Lists are ordered collection of data items
# They store multiple items in a single variable
# List items are separated by commas and enclosed within square brackets []
# Lists are changeable/mutable meaning we can alter them after creation
lst1 = [1,2,3,5,4,6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)

details = ["Abhijeet", 18, "FYBScIT", 9.8]
print(details)


# list index
# Each item/element in a list has its own unique index
# starts from --> [0], use [] to access
colors = ["Red", "Green", "Blue", "Yellow", "Black"]
#          [0]      [1]     [2]      [3]      [4]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[2])
print(colors[4])
print(colors[0])
# negative indexing, last element --> [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])

# verify presence in list using 'in' keyword
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")


# range of index
# You can print a range of list items by specifying 
# where you want to start, where do you want to end 
# and if you want to skip elements in between the range
# listName[start : end : jumpIndex]
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	    #using positive indexes
print(animals[-7:-2])	#using negative indexes

print(animals[4:])	    #using positive indexes
print(animals[-4:])	    #using negative indexes

print(animals[:6])	    #using positive indexes
print(animals[:-3])	    #using negative indexes

print(animals[::2])		#jumping indexes
print(animals[-8:-1:2])	#using negative indexes

print(animals[1:8:3])


################################################
# List Comprehension

# List comprehensions are used for creating new lists 
# from other iterables like lists, tuples, dictionaries, 
# sets, and even in arrays and strings

# List = [Expression(item) for item in iterable if Condition]
# Expression: It is the item which is being iterated.
# Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.
# Condition: Condition checks if the item should be added to the new list or not.

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [itemy for itemy in names if (len(itemy) > 4)]
print(namesWith_O)

# read as "for 'entity' in 'list' if 'given codition is satisfied' return 'entity' 
# in item mentioned at beginning"

print('\n')

##################################################################################
# list methods

# list.sort()
# sorts the list in ascending order
######################################################### original list is changed
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)
colors.sort(reverse=True)   # descending order
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)
num.sort(reverse=True)      # descending order
print(num)

# reverse parameter is set to False by default
print('\n')


# list.reverse()
# This method reverses the order of the list
colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)

print('\n')

# list.index()
# This method returns the index of the first occurrence of the list item
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(9))

print('\n')

# list.count()
# returns the count of the number of items with the given value
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.count(2))

print('\n')

# list.copy()
# Returns copy of the list. 
# This can be done to perform operations on the list without modifying the original list.
colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)

print('\n')

# list.append()
# This method appends items to the end of the existing list
colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors)

print('\n')

# list.insert()
# This method inserts an item at the given index. 
# User has to specify index and the item to be inserted within the insert() method.
colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]
print(colors)
colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]
print(colors)

print('\n')

# list.extend()
# This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list
# add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)

print('\n')

# concatenate two lists
colors1 = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors1 + colors2)