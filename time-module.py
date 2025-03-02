# The time module in Python provides a set of functions to work with time-related operations, 
# such as timekeeping, formatting, and time conversions.
import time

# The time.time() function returns the current time as a floating-point number, 
# representing the number of seconds since the epoch (the point in time when the time module was initialized). 
# The returned value is based on the computer's system clock.
print(time.time())      # time stamp
print(time.localtime())

# The time.sleep() function suspends the execution of the current thread for a specified number of seconds. 
# This function can be used to pause the program for a certain period of time, allowing other parts of the program to run, 
# or to synchronize the execution of multiple threads.
print("Start:", time.time())
time.sleep(2)
print("End:  ", time.time())

# The time.strftime() function formats a time value as a string, based on a specified format. 
# This function is particularly useful for formatting dates and times in a human-readable format, 
# such as for display in a GUI, a log file, or a report.
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
# the function time.strftime() formats the current time (obtained using time.localtime()) as a string, using a specified format. 
# The format string contains codes that represent different parts of the time value, 
# such as the year, the month, the day, the hour, the minute, and the second.
print(formatted_time)


# timekeeping using loop

def usingWhile():
    i = 0
    while i<50000:
        i = i + 1
        print(i)    # without printing, the execution of this loop takes close to 0 sec

def usingFor():
    i = 0
    for i in range(50000):
        print(i)    # without printing, the execution of this loop takes close to 0 sec

init1 = time.time()
usingWhile()
t1 = time.time() - init1
init2 = time.time()
usingFor()
t2 = time.time() - init2
print('while loop: ', t1)
print('for loop: ', t2)

# for loop is faster