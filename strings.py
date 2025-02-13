name = "Gautam"
print("Hello, " + name)

# strings can be enclosed in single or double quotes
print('He said, "I want to eat an apple".')

# multi-line string, triple quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# In Python, string is like an array of characters
# indexing starts at 0
# access characters in a string
print(name[0])
print(name[1])

print('\n')

# We can loop through strings using a for loop
for character in name:
    print(character)

print('\n')

# length of a string
fruit = "Mango"
# len1 = len(fruit)
print("Mango is a", len(fruit), "letter word.")


###########################################################
# string slicing

# A string is essentially a sequence of characters also called an array. 
# Thus we can access the elements of this array.

pie = "ApplePie"
print(len(pie))
print(pie[6])	#returns character at specified index

print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between     
# including 2 but not 6

print(pie[-8:])     #Slicing using negative index   # same as print(pie[len(pie)-8:])
print(pie[len(pie)-8:])


#################################################
# loop through a string
# Strings are arrays and arrays are iterable. 
# Thus we can loop through strings.
alphabets = "ABCDE"
for i in alphabets:
    print(i)