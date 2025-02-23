# map, filter, and reduce functions are built-in functions that allow you to 
# apply a function to a sequence of elements and return a new sequence. 
# These functions are known as higher-order functions, as they take other functions as arguments.

# MAP Function

# The map function applies a function to each element in a sequence and returns a new sequence 
# containing the transformed elements. The map function has the following syntax
# map(function, iterable)

# The function argument is a function that is applied to each element in the iterable argument. 
# The iterable argument can be a list, tuple, or any other iterable object.
numbers = [1,2,3,4,5]
# print(numbers)

cubed = map(lambda x : x**3, numbers)
# print(type(double))     # output class --> map
# typecast into list
print(list(cubed))

# same process using for loop
# # def cube(x):
# #   return x * x * x


# # print(cube(2))

# l = [1, 2, 4, 6, 4, 3]
# # newl = []
# # for item in l:
# #   newl.append(cube(item))


# FILTER Function

# filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) 
# and returns a new sequence containing only the elements that meet the predicate. 
# The filter function has the following syntax:
# filter(predicate, iterable)
# predicate argument is a function that returns a boolean value
numbers = [1,2,3,4,5]

evens = filter(lambda x : x%2==0, numbers)
print(list(evens))


# REDUCE Function

# reduce function is a higher-order function that applies a function to a sequence and returns a SINGLE VALUE 
# It is a part of the functools module in Python and has the following syntax:
# reduce(function, iterable)
# reduce function applies the function to the first two elements in the iterable and then applies the function 
# to the result and the next element, and so on. The reduce function returns the final result.
numbers = [1,2,3,4,5]

from functools import reduce    # reduce function requires the functools module to be imported in order to use it

sum = reduce(lambda x,y : x+y, numbers)     # reduces to single entry
print(sum)