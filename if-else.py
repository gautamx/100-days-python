# if statement
a = 23      #int(input("Enter your age: "))
print("Your age is:", a)

if(a>18):
  print("You can drive")
else:
  print("You cannot drive")


# if-else statement
applePrice = 10
budget = 200
if (budget-applePrice >= 50):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")


# elif statement
num = -25        #int(input("Enter the value of num: "))
if (num < 0):
  print("Number is negative.")
elif (num == 0):
  print("Number is Zero.")
elif (num == 999):
  print("Number is Special.")
else:
  print("Number is positive.")


# nested-if statement
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")



###########################################################
# if-else shorthand
# can be used when the condition being tested is simple 
# and the code blocks to be executed are short.
a = 10
b = 30
print('a is greater') if ( a > b ) else print('b is greater')

# multiple else statements on the same line
print('a is greater than') if ( a > 15 ) else print ('a is equal to 15') if ( a==b ) else print('a is less than 15')


# another usecase

# result = value_if_true if condition else value_if_false
c = 100 if ( a > b ) else 17
print(c)

# same as
# if condition:
#     result = value_if_true
# else:
#     result = value_if_false