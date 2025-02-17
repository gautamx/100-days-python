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
