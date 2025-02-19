# Dictionaries are ordered collection of data items. They store multiple items in a single variable. 
# Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

# Accessing Dictionary items

# Accessing single values
# Values in a dictionary can be accessed using keys.
print(info['name'])
print(info.get('eligible'))

# Accessing multiple values
# We can print all the values in the dictionary using values() method.
print(info.values())

# Accessing keys
print(info.keys())

# Accessing key-value pairs
print(info.items())         # all key-value pairs


for key in info.keys():
    print(f'The value corresponding to {key} is {info[key]}')

for key, value in info.items():
    print(f'The value corresponding to {key} is {value}')


###################################################################
# dictionary methods

# update()
# updates the value of the key provided to it if the item already exists in the dictionary, 
# else it creates a new key-value pair
info.update({'age':20})
info.update({'DOB':2001})
print(info)

# clear()
# removes all the items from the list
info.clear()
print(info)

# pop() 
# removes the key-value pair whose key is passed as a parameter
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)

# popitem() 
# removes the last key-value pair from the dictionary
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)

# del
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)
# If key is not provided, then the del keyword will delete the dictionary entirely
# del info
# print(info)