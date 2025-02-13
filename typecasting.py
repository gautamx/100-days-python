# explicit typecasting

a="1"
b="2"
print(a+b)              #string concatenation
print(int(a)+int(b))    #int addition


string = "15"
number = 7
#sum = string + number     #throws an error because different datatype
string_number = int(string) #throws an error if the string is not a valid integer
sum = number + string_number
print("The Sum of both the numbers is: ", sum)


# implicit typecasting

# Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))