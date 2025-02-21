def function():
    print('This is a function.')

string = 'This is a string.'


if __name__ == "__main__":
    def main():
        print('This is the main function.')

    main()


# if __name__ == "__main__" idiom is a common pattern 
# used in Python scripts to determine whether the script 
# is being run directly or being imported as a module into another script

# __name__ variable is a built-in variable that is automatically set to the name of the current module. 
# When a Python script is run directly, the __name__ variable is set to the string __main__ 
# When the script is imported as a module into another script, the __name__ variable is set to the name of the module

# syntax
# code:
# if __name__ == "__main__"
#       code that should execute only if the script is run directly

# This can be useful if you have code that you want to reuse in multiple scripts, 
# and some other code you only want to run when the script is run directly 
# and not when it's imported as a module within the same script
