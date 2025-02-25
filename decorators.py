# Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. 
# They are a way to extend the functionality of a function or method without modifying its source code.

# A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. 
# The new function is often referred to as a "decorated" function. The basic syntax for using a decorator is the following:

# @decorator_function
# def my_function():
#     pass

# @decorator_function notation is just a shorthand for the following code

# def my_function():
#     pass
# my_function = decorator_function(my_function)

# Decorators are often used to add functionality to functions and methods, such as logging, memoization, and access control.

#######################################################################################################################################################

# example
# Basic decorator
def my_decorator(func):
    def wrapper():
        print("Something happens before the function is called.")
        func()
        print("Something happens after the function is called.")
    return wrapper

# Using the decorator with @ syntax
@my_decorator
def say_hello():
    print("Hello!")

# When you call say_hello(), it's actually calling the wrapped version
say_hello()
# Output:
# Something happens before the function is called.
# Hello!
# Something happens after the function is called.


# Practical use case --> logging
import logging

def log_function_call(func):
    def wrapper(*args,**kwargs):
        # logging.info(f'Calling {func.__name__} with args={args} and kwargs={kwargs}')
        print(f'Calling {func.__name__} with args={args} and kwargs={kwargs}')
        result = func(*args,**kwargs)
        # logging.info(f'{func.__name__} returned {result}')
        print(f'{func.__name__} returned {result}')
        return result
    return wrapper

@log_function_call
def my_func(a,b,c):
    return a+b+c

print(my_func(10,20,30))

# tool for separating concerns, reducing code duplication, and making your code more readable and maintainable.
# python decorators are a way to extend the functionality of functions and methods, by modifying its behavior without modifying the source code.

# another example
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hi(name):
    print(f"Hi {name}!")
    
say_hi("Gautam")
# repeat(say_hi("Yukio"))

@repeat(5)
def sum(a,b,c):
    print(a+b+c)

sum(1,2,3)
# repeat(sum(4,5,6))