# Importing in Python is the process of loading code from a Python module into the current script. 
# This allows you to use the functions and variables defined in the module in your current script, 
# as well as any additional modules that the imported module may depend on.

import math

# you can use any of the functions and variables defined in the module by using the dot notation
result = math.sqrt(9)
print(result)

# import specific functions or variables from a module using the 'from' keyword
# import multiple functions or variables at once by separating them with a comma
from math import sqrt, pi
result = sqrt(9)
print(result)
print(pi)

# possible to import all functions and variables from a module using the * wildcard
# not recommended, as you cannot follow where a function is coming from
from math import *
print(pow(2,3))

# rename imported modules using the 'as' keyword
import math as m
print(m.sin(pi/2))

# built-in function called dir that you can use to view the names of all the functions and variables defined in a module
print(dir(math))        # outputs a list


print('\n')
######################################################
# using a custom test module
import testModule as tm
print(dir(tm))

tm.function()
print(tm.string)# Importing in Python is the process of loading code from a Python module into the current script. 
# This allows you to use the functions and variables defined in the module in your current script, 
# as well as any additional modules that the imported module may depend on.

import math

# you can use any of the functions and variables defined in the module by using the dot notation
result = math.sqrt(9)
print(result)

# import specific functions or variables from a module using the 'from' keyword
# import multiple functions or variables at once by separating them with a comma
from math import sqrt, pi
result = sqrt(9)
print(result)
print(pi)

# possible to import all functions and variables from a module using the * wildcard
# not recommended, as you cannot follow where a function is coming from
from math import *
print(pow(2,3))

# rename imported modules using the 'as' keyword
import math as m
print(m.sin(pi/2))

# built-in function called dir that you can use to view the names of all the functions and variables defined in a module
print(dir(math))        # outputs a list


print('\n')
######################################################
# using a custom test module
import testModule as tm
print(dir(tm))      # does not show attributes under if-name-main

tm.function()
print(tm.string)

# we cannot execute the main() outside the module/script
tm.main()