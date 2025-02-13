# input function takes the input & gives a return value 
# as string/character hence we have to pass that into a variable
a = input("Enter your name: ")
print("Your name is", a)

x = input("Enter first number: ")
y = input("Enter second number: ")
# input is string, '+' concatenates
print(x + y,"concatenation")
# typecast as int to add
print("sum of x and y is", int(x) + int(y))

# or do it like this
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))