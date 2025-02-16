# while loops execute statements while the condition is True
i = 0
while(i < 5):
    print(i+1, end=" ")
    i+=1

print('\n')

# for loop syntax is sometimes more convenient
for k in range(5):              # same as range(0, 5)
    print(k+1, end=" ")

print('\n')

# decrementing while loop
i = 5
while(i > 0):
    print(i, end=" ")
    i-=1                
# if i is incremented instead of decrementing then it will 
# create an infinite loop

print('\n')

# else statement with the while loop
i = 5
while(i > 0):
    print(i)
    i-=1
else:       # executed when while condition becomes false
    print("counter is zero")


###########################################################
# python does not have do-while loop
# do..while is a loop in which a set of instructions will 
# execute at least once (irrespective of the condition)
# exit-controlled loop

# do-while syntax
# do{
#    loop body
# }while(condition)
# loop body is executed once before checking for the condition

# how to emulate a do-while loop in python
# use an infinite while loop with a break statement wrapped in an 
# if statement
while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break
  
i = 10
while True:
  print(i, end=' ')
  i -= 1
  if not i > 0:
    break