# enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) 
# and get the index and value of each element in the sequence at the same time.
# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    # print(index, fruit)
    for idex, c in enumerate(fruit):
       print(c, end=' ')
    print('\n')

# enumerate function returns a tuple
# use for loop to unpack these tuples and assign them to variables

# change the starting index
# default is 0
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')


# Loop over a tuple and print the index and value of each element
colors = ('red', 'yellow', 'blue')
for index, color in enumerate(colors):
    print(index+1, color)

# with string
str = 'hello'
for index, letter in enumerate(str):
    print(index+1, letter)


# example
marks = [12, 56, 32, 98, 12,  45, 1, 4]

# index = 0
# for mark in marks:
#   print(mark)
#   if(index == 3):
#     print("Harry, awesome!")
#   index +=1

for index, mark in enumerate(marks, start=1):
  print(mark)
  if(index == 3):
    print("Harry, awesome!")