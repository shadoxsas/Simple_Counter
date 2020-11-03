#import section
import time
import os

def timer():
    conversion = hrs*3600 + mins*60 + secs
    while conversion != 0:
        for i in range(conversion,0,-1):
            if i >= 3600:
                h = conversion // 3600
                min = int((conversion / 3600 - h) * 60 // 1)
                sec = int(round((((conversion / 3600 - h) * 60) - min) * 60, 0))
                print(f'Remaining time: {h} h {min} min {sec} s')
                conversion = conversion - 1
                time.sleep(1)
            elif 3599 >= i >= 60:
                h = conversion // 3600
                min = int((conversion / 3600 - h) * 60 // 1)
                sec = int(round((((conversion / 3600 - h) * 60) - min) * 60, 0))
                print(f"Remaining time: {min}min {sec}s")
                conversion = conversion - 1
                time.sleep(1)
            else:
                h = conversion // 3600
                min = int((conversion / 3600 - h) * 60 // 1)
                sec = int(round((((conversion / 3600 - h) * 60) - min) * 60, 0))
                print(f"Remaining time: {sec}s")
                conversion = conversion - 1
                time.sleep(1)

    print("\nSTOP COUNTING")

def timer_meth():
    global dys, hrs, mins, secs
    while True:
        errors = 0
        try:
            #dys = int(input("Enter the numer of days: "))
            hrs = int(input("Enter the number of hours: "))
            mins = int(input("Enter the number of minutes: "))
            secs = int(input("Enter the number of seconds: "))
            print(f'The counter will count down by: {hrs} hours {mins} minutes {secs} seconds')
        except ValueError:
            print("An integer has not been entered. Please try again.")
        else:
            if mins >= 60:
                errors += 1
                print("Given number of minutes is higher thant 60")
            if mins < 0:
                errors += 1
                print("Given number of minutes is lower than 0")
            if hrs < 0:
                errors += 1
                print("Given number of hours is lower than 0")
            if secs >= 60:
                errors += 1
                print("Given number of seconds is higher thant 60")
            if secs < 0:
                errors += 1
                print("Given number of seconds is lower than 0")
            if not errors:
                break

timer_meth()
timer()



