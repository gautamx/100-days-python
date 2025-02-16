# break statement enables a program to skip over a part of the code
# break statement terminates the very loop it lies within
for i in range(1,21,1):
    print(i ,end=" ")
    if(i==10):
        break
    else:
        print("Mississippi")
print("\nEnd of loop\n")

# another example
for i in range(99):
    print( '5 x ',i+1,' = ',5*(i+1) )
    if( i == 9 ):
        break
print("End of loop\n")

# another example
for i in range(99):
    if( i == 10 ):
        break
    print( '5 x ',i+1,' = ',5*(i+1) )
print("End of loop\n")


##################################################
# continue statement skips to the next iteration
for i in range(99):
    if( i == 11 ):
        break
    if( i == 0 ):
        print('iteration skipped')
        continue  
    if( i % 2 != 0 ):
        print('iteration skipped')
        continue            
    # 'continue' should come before the executable statement 
    # in for loop, otherwise the statement will be executed
    print( '5 x ',i,' = ',5*i )
print("End of loop\n")
