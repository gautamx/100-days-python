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