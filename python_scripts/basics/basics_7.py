## Largest of Two Numbers 

### 1. Using Elif Statement

print("\nPython Program to find Largest of Two Numbers.\n")
print("\n------------------------------elif statements-----------------------------------\n")
 

a = float(input("Please Enter the First Value a: "))
b = float(input("Please Enter the Second Value b: "))

if(a > b):
    print("{0} is Greater than {1}".format(a, b))
elif(b > a):
    print("{0} is Greater than {1}".format(b, a))
else:
    print("Both a and b are Equal")
    
# * The first if condition checks whether a is greater than b. If True, then a is greater than b printed
# * Elif statement checks whether b is greater than a. If True, then b is higher than a printed
# * If all the above conditions fail, they are equal.

print("\n------------------------------nested if statements------------------------------\n")

if(a == b):
    print("Both a and b are Equal")
else:
    largest = a if a > b else b
    print("{0} is the Largest Value".format(largest))
    
print("\n------------------------------arithmetic operator-------------------------------\n")

if(a - b > 0):
    print("{0} is Greater than {1}".format(a, b))
elif(b - a > 0):
    print("{0} is Greater than {1}".format(b, a))
else:
    print("Both a and b are Equal")
