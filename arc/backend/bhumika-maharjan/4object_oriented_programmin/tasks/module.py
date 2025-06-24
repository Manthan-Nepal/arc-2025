# Use the os module to list all files in the current directory.
# Use the datetime module to find the difference between two dates in days.
import os
import datetime
 
list = os.listdir()

print(list)

difference = datetime.datetime(2025, 5, 29)-datetime.datetime(2025,5,27)
print(difference)