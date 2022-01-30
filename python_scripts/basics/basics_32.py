## Current Date and Time

print("\n Current Date and Time \n")

from datetime import date, datetime

today = date.today()
print("Current Date = ", today)

today = datetime.now()
print("Current Date and Time = ", today)

# Formatting Date and Time
dt = today.strftime("%B %d, %Y - %H:%M:%S")
print("Current Date and Time with format %B %d, %Y - %H:%M:%S= ", dt)

dt = today.strftime("%m/%d/%Y, %H:%M:%S")
print("Current Date and Time with format %m/%d/%Y, %H:%M:%S= ", dt)