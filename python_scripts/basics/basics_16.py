## Python Program to find Square root of a Number

### 1. Using sqort() function in math library

import math

print("\nProfit or loss\n")
print("\n------------------------------with sqrt()---------------------------------------\n")

number = float(input("Please enter anyumerical value:"))
square_root = math.sqrt(number)
print("The Square Root of a Given Number {0}  = {1}".format(number, square_root))

### 2. Using pow() from math library

print("\n------------------------------with pow()---------------------------------------\n")

number = float(input("Please enter anyumerical value:"))
square_root = math.pow(number,0.5)
print("The Square Root of a Given Number {0}  = {1}".format(number, square_root))