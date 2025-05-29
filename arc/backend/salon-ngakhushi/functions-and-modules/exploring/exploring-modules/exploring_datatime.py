import time
import datetime as dt

def count(start, end=3):
    for x in range(start, end+1):
        print(x)
        time.sleep(2)
    print("Prints every 2 seconds!")
    
count(0)

current_date_and_time= dt.datetime.now()
print(current_date_and_time)

custom_date= dt.date(2027, 5, 17)
print(custom_date)

custom_time= dt.time(17, 30, 42)
print(custom_time)

format_date= current_date_and_time.strftime(f"\nDate: %Y-%m-%d \nTime: %H:%M:%S.%f")[:-4]
print(format_date)