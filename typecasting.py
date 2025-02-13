# explicit typecasting

string = "15"
number = 7
#sum = string + number     #throws an error because different datatype
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)