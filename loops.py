# FOR LOOPS can iterate over a sequence of iterable objects

name = 'Abhishek'
for i in name:
    print(i, end=" ")
    # if(i=="i"):
    #     print("break\n")

# print('\n')

colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    #print(x)
    print('\n')
    for i in x:
        print(i, end=' ')

print('\n')

# execute a loop for a certain range
for k in range(5):              # same as range(0, 5)
    print(k, end=" ")

print('\n')

for k in range(5):
    print(k+1, end=" ")

print('\n')

# second param in range --> length n

for k in range(0, 10):
    print(k, end=" ")

print('\n')

for k in range(1, 10):
    print(k, end=" ")

print('\n')

# third param in range --> step

for k in range(2, 50, 11):
    print(k, end=" ")

print('\n')

for k in range(2, 50):
    if( (k-2) % 11 == 0 ):      # what the third param does internally
        print(k, end=" ")