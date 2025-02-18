# In Python, a function can call another function. 
# It is even possible for a function to call itself. 
# These types of construct are termed as recursive functions.

# program to calculate factorials
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return (n * factorial(n-1))     # recursion
    
print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1

# a program to print the Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)
# 0 1 1 2 3 5 8....
def fibonacci(n):
    if (n<=1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num_terms = 10           # int(input('How many terms in Fibonacci Sequence? '))
# print(range(num_terms))
for i in range(num_terms): 
    print(fibonacci(i), end=' ') 