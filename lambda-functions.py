# a lambda function is a small anonymous function without a name

# syntax
# lambda arguments: expression

# used in situations where a small function is required for a short period of time. 
# They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.

# function to double the input
def double(x):
    return x*2

# lambda function to double the input
lambda x : x*2      # the lambda function is anonymous, as it does not have a name


# multiple arguments
def multiply(x,y):
    return x*y

lambda x,y : x*y


lambda x,y : print(f'{x} * {y} = {x*y}')


###################################################################################
double = lambda x : x*2
cube = lambda x : x**3
avg = lambda x,y,z : (x+y+z)/3

print(double(5))
print(cube(5))
print(avg(5,10,15))

def appl(fx, value):
    return 10 + fx(value)

print(appl(lambda x : x**2, 2))