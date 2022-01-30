##  Print Natural Numbers

### 1. Using for loop

print("\nPython Program to Print Natural Numbers from 1 to N\n")

print("\n---------------------------using for loop---------------------------------------\n")

number = int(input("Please Enter any Number: "))

print("The List of Natural Numbers from 1 to {0} are".format(number)) 
for i in range(1, number + 1):
    print (i, end = '  ')
    
print("\n---------------------------using while loop-------------------------------------\n")

i = 1

print("The List of Natural Numbers from 1 to {0} are".format(number)) 

while ( i <= number):
    print (i, end = '  ')
    i = i + 1