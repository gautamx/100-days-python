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

f.write("\nTrue beauty is something that attacks, overpowers, robs, and finally destroys.\n")

f.close()

f = open("file2.txt", "r")

contents = f.read()
print(contents)


# alternatively, use 'with' statement
with open('file2.txt', 'a') as f:
    f.write("\nBeauty is something that burns the hand when you touch it.\n")