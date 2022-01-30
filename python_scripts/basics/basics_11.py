## Check Leap Year 

# Note: A century year cannot be a leap year unless it is divisible by 400.

### 1. Using If Statement

print("\n--------------------------Using If Statement------------------------------------\n")

year = int(input("Please Enter the Year Number you wish: "))

if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
    print("%d is a Leap Year" %year)
else:
    print("%d is Not a Leap Year" %year)
    
print("\n--------------------------Using elif Statement----------------------------------\n")

if (year%400 == 0):
          print("%d is a Leap Year" %year)
elif (year%100 == 0):
          print("%d is Not a Leap Year" %year)
elif (year%4 == 0):
          print("%d is a Leap Year" %year)
else:
          print("%d is Not a Leap Year" %year)
        
print("\n--------------------------Using nested if---------------------------------------\n")

year = int(input("Please Enter the Year Number you wish: "))

if(year%4 == 0):
    if(year%100 == 0):
        if(year%400 == 0):
            print("%d is a Leap Year" %year)
        else:
            print("%d is Not the Leap Year" %year)
    else:
        print("%d is a Leap Year" %year)
else:
    print("%d is Not the Leap Year" %year)