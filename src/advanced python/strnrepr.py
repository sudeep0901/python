import datetime 
import time

today = datetime.datetime.now()

str(today)
repr(today)

# You can see that this also returned a string but the string was the “official” representation of a datetime object. What does official mean? Using the “official” string representation I can reconstruct the object
eval('datetime.datetime(2012, 3, 14, 9, 21, 58, 130922)')
print(chr(71), chr(101))

for i in range(10000):
    print(chr(int(i)), i)
    time.sleep(1/100)








