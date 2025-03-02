




# run this script from cmd line with a positional arg
# python "D:\Code\100-days-python\cmd-line-utility.py" my_positional_value





# Command line utilities are programs that can be run from the terminal or command line interface, 
# and they are an essential part of many development workflows. 
# In Python, you can create your own command line utilities using the built-in argparse module.
import argparse

#######################################         SYNTAX

# # add cmd line arguments
# parser.add_argument('arg1', help='description of argument 1')
# parser.add_argument('arg2', help='description of argument 2')

# # parse the arguments
# args = parser.parse_args()

# # use the arguments in code
# print(args.arg1)
# print(args.arg2)

#######################################

# adding optional args to cmd line utility
parser = argparse.ArgumentParser()

# adding optional args to cmd line utility
parser.add_argument('-o', '--optional', help="description of optional argument", default="default_optional")
# adding positional argument
parser.add_argument('positional', help='description of positional argument')
# adding arguments with type
parser.add_argument("-n", type=int, help="description of integer argument")

args = parser.parse_args()

print(args.optional)
print(args.positional)
print(args.n)
