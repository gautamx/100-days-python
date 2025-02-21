# os module in Python is a built-in library that provides functions for interacting with the operating system
# helps in reading and writing files, interacting with the file system, and running system commands

import os

# functions for opening, reading, and writing files

# open file in read-only mode
f = os.open("file1.txt", os.O_RDONLY)

# read the contents of the file
contents = os.read(f, 1024)

# close the file
os.close(f)

print(contents)
print(type(contents))


# open file in write-only mode
f = os.open("file1.txt", os.O_WRONLY)

string = '''a small night storm blows
saying, "Falling is the essence of a flower",
preceding those who hesitate\n'''
string_as_bytes = str.encode(string)        # encoding string into bytes
# string_as_bytes.decode()                  # decoding bytes into string

# writing to a file
numBytes = os.write(f, string_as_bytes)
print('Number of bytes written: ', numBytes)

# close the file
os.close(f)


# open file in append mode
f = os.open("file1.txt", os.O_WRONLY | os.O_APPEND)  # Need O_WRONLY for write operations

string2 = '''\nTrue beauty is something that attacks, overpowers, robs, and finally destroys.\n'''
string2_as_bytes = string2.encode()  # str.encode(string2) works too, but string2.encode() is more common

# appending to a file is just writing in append mode
os.write(f, string2_as_bytes)

# close the file
os.close(f)


# with built-in open() function
# # Method 1: Using 'with' statement (recommended)
# with open("file1.txt", "a") as f:
#     f.write("True beauty is something that attacks, overpowers, robs, and finally destroys.\n")

# # Method 2: Traditional open/close method
# f = open("file1.txt", "a")
# f.write("True beauty is something that attacks, overpowers, robs, and finally destroys.\n")
# f.close()


# interacting with the file system

# get a list of files in directory
print(os.listdir('.'))

# create a new directory
# os.mkdir('newdir')


# running system commands

# Basic command
os.system('echo Hello World')

# Directory operations
print(os.system("dir"))       # "ls" for linux/mac

# getting output in file-like object
f = os.popen("dir")
print(f.read())
f.close()       # close file-like object


# some applications

# if(not os.path.exists("data")):
#     os.mkdir("data")
# for i in range(100):
#     os.mkdir(f"data/day{i+1}")

# current working directory
print(os.getcwd())

# change working directory
# os.chdir("/path")
# print(os.getcwd())

# folders = os.listdir("data")
# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))

# for i in range(100):
#     os.rename(f"data/tutorial{i+1}", f"data/tutorial {i+1}")