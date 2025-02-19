# Python allows the else keyword to be used with the for and while loops too. 
# The else block appears after the body of the loop. 
# The statements in the else block will be executed after all iterations are completed. 
# The program exits the loop only after the else block is executed.
for x in range(5):
    print('iteration number {} in for loop'.format(x+1))
else:
    print('now in else block')
print('out of loop')


# can be done with while loop as well
i = 0
while i<7:
  print(i)
  i = i + 1
#   if i == 4:
#     break         # if you break while loop else will not be executed
else:
  print("Sorry no i")

# the 'else' block is part of the loop