# import os
# os.system("python --version")

# MATCH CASE STATEMENTS
# A match statement will compare a given variable’s 
# value to different shapes, also referred to as the 
# pattern. The main idea is to keep on comparing the 
# variable with all the present patterns until it 
# fits into one.

x = int(input("Enter x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty/Default case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    
    case _ if x!=100:
        print("x is not equal to 100")

    case _ if x!=75:
        print("x is not equal to 75")
    
    case _:         # default statement like else
        print(x)

# you can have multiple default statements
# just like if-else

# only executes one case statement 
# unlike in C where a break statement is needed