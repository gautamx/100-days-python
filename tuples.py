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