# Tuples are ordered collection of data items. 
# They store multiple items in a single variable. 
# Tuple items are separated by commas and enclosed within round brackets ().
# Tuples are unchangeable/immutable meaning we can not alter them after creation.
tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)

details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)

# tuple index
country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]       POSITIVE INDEXING
#            [-5]     [-4]     [-3]      [-2]       [-1]      NEGATIVE INDEXING
print(country[0])         
print(country[1])         
         
print(country[-1])      # Similar to print(country[len(country) - 1])
print(country[-3]) 


# Check for item in tuple
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")

if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")


# Range of Index:
# You can print a range of tuple items by specifying where do you want to start,
# where do you want to end and if you want to skip elements in between the range
# tuple[start : end : jumpIndex]
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     #using positive indexes
print(animals[-7:-2])   #using negative indexes

print(animals[4:])      
print(animals[-4:])   

print(animals[:6])     
print(animals[:-3])    

#using jump index
print(animals[::2])         # print alternate values 
print(animals[-8:-1:2]) 
print(animals[1:8:3])       # print every third value



###################################################################################
# Manipulating Tuples
# Tuples are immutable, hence if you want to add, remove or change tuple items, 
# then first you must convert the tuple to a list. 
# Then perform operation on that list and convert it back to tuple.
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       # add item
temp.pop(3)                 # remove item "England"
temp.insert(2, "Finland")   # insert item
countries = tuple(temp)
print(countries)

# we can directly concatenate two tuples without converting them to list
countries1 = ("Pakistan", "Afghanistan", "Bangladesh", "Sri Lanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries1 + countries2
print(southEastAsia)


####################################################################################
# Tuple Methods
# As tuple is immutable type of collection of elements it have limited built in methods

# tuple.count()
# returns the number of times the given element appears in the tuple
tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)

# tuple.index()
# returns the first occurrence of the given element from the tuple
hres = tuple1.index(3)
print('First occurrence of 3 is at index', hres)