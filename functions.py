# function is a block of code that performs a specific task whenever it is called
# built-in & user-defined functions

# def function_name(parameters):
#   pass
#   # Code and Statements

def name(fname, lname):
    print("Hello,", fname, lname)

name("Sam", "Wilson")

def calMean(a,b):
    mean=(a+b)/2
    print(mean)

calMean(76,99)

def isGreater(a,b):
    pass            # to add fn code later



############################################
# function arguments
############################################

# default arguments

# We can provide a default value while creating a function
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")
name("Amy", "David", "Madrigal")    
# if you pass args, default ones are overwritten 


# keyword arguments

# We can provide arguments with key = value, this way 
# the interpreter recognizes the arguments by the parameter name 
# Hence, the the order in which the arguments are passed does not matter
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")


# required arguments

# In case we don’t pass the arguments with a key = value syntax, 
# then it is necessary to pass the arguments in the correct positional order 
# and the number of arguments passed should match with actual function definition
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

# name("Peter", "Quill")        # will throw error
name("Peter", "Ego", "Quill")


# variable-length arguments

# Arbitrary Arguments
# While creating a function, pass a * before the parameter name while defining the function. 
# The function accesses the arguments by processing them in the form of TUPLE
def name(*name):
    print(type(name))
    print("Hello,", name[0], name[1], name[2])

# name("James", "Buchanan")     # throws error, tuple index out of range
name("James", "Buchanan", "Barnes") 
name("James", "Buchanan", "Barnes", "Vijay")    # ignores everything past index


def sumNum1(*num):
    i=0
    sum=0
    while(i<len(num)):
        sum = sum + num[i]
        i+=1
    print(sum)

def sumNum2(*num):
    sum=0
    for i in num:
        sum = sum + i
    print(sum)

sumNum1(5,9,8,100)
sumNum2(5,9,8,100)


# Keyword Arbitrary Arguments
# While creating a function, pass a ** before the parameter name while defining the function. 
# The function accesses the arguments by processing them in the form of DICTIONARY
def name(**name):
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])

# name(mname = "Buchanan", lname = "Barnes")
name(mname = "Buchanan", lname = "Barnes", fname = "James")


####################################################
# return statement
# return statement is used to return the value of the expression back to the calling function
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))

def sumNum(*num):
    sum=0
    for i in num:
        sum = sum + i
    return sum

print("Sum is", sumNum(5,9,8,100))