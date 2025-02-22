# Python provides the open() function to open a file. 
# It takes two arguments: the name of the file and the mode in which the file should be opened.
# The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.
# f = open("file2.txt", "r")

# By default, the open() function returns a file object
# that can be used to read from or write to the file, depending on the mode

# Modes: read (r), write (w), append (a)
# create (x): This mode creates a file and gives an error if the file already exists
# text (t): t refers to the text mode. There is no difference between r and rt or w and wt
# since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' )
# binary (b): used to handle binary files (images, pdfs, etc)

f = open("file2.txt", "x")      # create the file

f = open("file2.txt", "w")

print(f)

f.write('''a small night storm blows
saying, "Falling is the essence of a flower",
preceding those who hesitate\n''')

f.close()
# Important to close a file after you are done with it. 
# This releases the resources used by the file and allows other programs to access it.

f = open("file2.txt", "a")

f.write("True beauty is something that attacks, overpowers, robs, and finally destroys.\n")

f.close()

f = open("file2.txt", "r")

contents = f.read()
print(contents)


# alternatively, use 'with' statement
with open('file2.txt', 'a') as f:
    f.write("Beauty is something that burns the hand when you touch it.\n")


# readline()
# readline() method reads a single line from the file. 
# If we want to read multiple lines, we can use a loop.
f = open('file2.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)

# readlines() method reads all the lines of the file and returns them as a list of strings

# writelines()
# writelines() method in Python writes a sequence of strings to a file. 
# The sequence can be any iterable object, such as a list or a tuple.
# 
# f = open('myfile.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()

# writelines() method does not add newline characters between the strings in the sequence. 
# If you want to add newlines between the strings, you can use a loop to write each string separately
f = open('file2.txt', 'a')
lines = ['Another eye', 'Another heart', 'Another life']
for line in lines:
    f.writelines(line + '\n')
f.close()


f = open('file3.txt', 'r')
i=0
while True:
    i += 1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(',')[0])
    m2 = int(line.split(',')[1])
    m3 = int(line.split(',')[2])
    print(f"Marks of student {i} in Maths is: {m1}")
    print(f"Marks of student {i} in Physics is: {m2}")
    print(f"Marks of student {i} in Chemistry is: {m3}")
f.close()



#########################################################################
# seek() and tell() functions are used to work with file objects and their positions within a file

# seek() function allows you to move the current position within a file to a specific point. 
# The position is specified in bytes, and you can move either forward or backward from the current position
with open('file2.txt', 'r') as f:
    # Move to the 10th byte in the file
    f.seek(10)
    # Read the next 5 bytes
    data = f.read(50)
    print(data)

# tell() function returns the current position within the file, in bytes. 
# This can be useful for keeping track of your location within the file 
# or for seeking to a specific position relative to the current position.
    # Save the current position
    current_position = f.tell()
    # seek the current position
    print(current_position)
    print( f.seek(current_position) )
    f.close()

# with open('file2.txt', 'w') as f:
#     f.seek(10)
#     # if you want to truncate the file to a specific size, you can use the truncate function.
#     f.truncate(200)       # can be done in 'w' or 'a' mode
#     print(f.read)
#     f.close()