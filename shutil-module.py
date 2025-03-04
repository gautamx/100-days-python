# Shutil is a Python module that provides a higher level interface for working with file and directories. 
# The name "shutil" is short for shell utility. 
# It provides a convenient and efficient way to automate tasks that are commonly performed on files and directories.
import shutil
import os

# This function copies the file located at src to a new location specified by dst. 
# If the destination location already exists, the original file will be overwritten.

shutil.copy('shutil-module.py', 'shutil-module-2.py')

# This function is similar to shutil.copy, 
# but it also preserves more metadata about the original file, such as the timestamp.

shutil.copy2('shutil-module.py', 'shutil-module-2.py')

# This function recursively copies the directory located at src to a new location specified by dst. 
# If the destination location already exists, the original directory will be merged with it.

# shutil.copytree("shutil-src", "shutil-dst")

# This function moves the file located at src to a new location specified by dst. 
# This function is equivalent to renaming a file in most cases.

# shutil.move("shutil-src\src.txt", "shutil-src\src2.txt")

# This function recursively deletes the directory located at path, along with all of its contents. 
# This function is similar to using the rm -rf command in a shell.

# shutil.rmtree("shutil-dst")

# os.remove("shutil-dst")   # access denied