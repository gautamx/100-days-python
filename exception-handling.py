# without exception handling, exceptions would disrupt the normal operation of a program.

# When exceptions occur, the Python interpreter stops the current process 
# and passes it to the calling process until it is handled. If not handled, the program will crash.

# try….. except blocks are used in python to handle errors and exceptions. 
# The code in try block runs when there is no error. 
# If the try block catches the error, then the except block is executed.
try:
    num = int(input('enter an integer: '))
except ValueError:
    print('the entered value is not an integer')

print("Some imp lines of code")
print("End of block")

try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
  print("Index Error")

print("Some more imp lines of code")
print("End of program")


# Finally Clause
# The finally code block is also a part of exception handling. 
# When we handle exception using the try and except block, 
# we can include a finally block at the end. 

# The finally block is always executed

# so it is generally used for doing the concluding tasks 
# like closing file resources
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")


def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")

x = func1()
print(x)


# Raising Custom Errors
# using the 'raise' keyword
salary = int(input('Enter salary amount: '))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")

# Defining Custom Exceptions
# we can define custom exceptions by creating a new class 
# that is derived from the built-in Exception class.
# 
# syntax:
# class CustomError(Exception):
#   # code ...
#   pass

# try:
#   # code ...

# except CustomError:
#   # code...