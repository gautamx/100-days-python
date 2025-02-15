# STRINGS ARE IMMUTABLE

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


#################################################
# String Methods

# upper() method converts a string to upper case
str1 = "AbcDEfghIJ"
print(str1.upper())

# lower() method converts a string to lower case
print(str1.lower())

# strip() method removes any white spaces 
# before and after the string
str2 = "          Silver Spoon                     "
print(str2.strip())

# rstrip() removes any trailing characters
str3 = "Hello#######"
print(str3.rstrip("#"))

# replace() method replaces all occurences 
# of a string with another string
str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))

# split() method splits the given string at the specified instance 
# and returns the separated strings as list items
str2 = "Silver Spoon"
print(str2.split(" "))      #Splits the string at the whitespace " ".

# capitalize() method turns only the first character of the 
# string to uppercase and the rest other characters 
# of the string are turned to lowercase.
str1 = "hello"
capStr1 = str1.capitalize()
print(capStr1)
str2 = "hello WOrlD"
capStr2 = str2.capitalize()
print(capStr2)

# center() method aligns the string to the center 
# as per the parameters given by the user
str1 = "Welcome to the Console!!!"
print(str1.center(150))
print(str1.center(150, "."))    # padding

# count() method returns the number of times the 
# given value has occurred within the given string
str2 = "strawberry"
countStr = str2.count("r")
print(countStr)

# endswith() method checks if the string ends with a given value
# returns true or false
str3 = " Hellloooo !!!!"
print(str3.endswith("."))
print(str3.endswith("!"))
# checking in-between a string with index position
str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))
print(str1.endswith("to", 4, 11))

# find() method searches for the first occurrence of the given value
# and returns the index where it is present 
# If given value is absent from the string then return -1
str1 = "His name is Dan. He is an honest man."
print(str1.find("dan"))
print(str1.find("Dan"))

# index() method searches for the first occurrence of the given value 
# and returns the index where it is present 
# If given value is absent from the string then raise an exception
str1 = "His name is Dan. Dan is an honest man."
# print(str1.index("dan"))  # raises exception
print(str1.index("Dan"))

# isalnum() method returns True only if the entire string only consists
# of A-Z, a-z, 0-9. If any other characters or punctuations are present, 
# then it returns False. whitespace --> false
str1 = "WelcomeToThe Console"
print(str1.isalnum())

# isalpha() method returns True only if the entire string only consists 
# of A-Z, a-z. If any other characters or punctuations or numbers(0-9) 
# are present, then it returns False
str1 = "Welcome"
print(str1.isalpha())

# islower() method returns True if all the characters in the string are 
# lower case, else it returns False
str1 = "hello world"
print(str1.islower())

# isprintable() method returns True if all the values within the given 
# string are printable, if not, then return False
# eg. \n is not a printable character
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())

# isspace() method returns True only and only if the string contains 
# white spaces, else returns False
str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())

# istitile() returns True only if the first letter of each word of the
# string is capitalized, else it returns False
str1 = "World Health Organization" 
print(str1.istitle())

# isupper() method returns True if all the characters in the string are 
# upper case
str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())

# startswith() method checks if the string starts with a given value
str1 = "Python is a Interpreted Language" 
print(str1.startswith("is"))

# swapcase() method changes the character casing of the string 
# Upper case are converted to lower case and lower case to upper case
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

# title() method capitalizes each letter of the word within the string
str1 = "His name is Dan. Dan is an honest man."
print(str1.title())