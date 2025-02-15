# greetings as per local time
import time
from time import strftime

print(strftime('%d/%m/%Y %H:%M:%S %Z'))

hour = int(strftime("%H"))
if( hour >= 4 and hour < 12 ):
    print("Good Morning")
elif( hour >= 12 and hour < 16 ):
    print("Good Afternoon")
elif( hour >= 16 and hour < 20 ):
    print("Good Evening")
else:
    print("Good Night")