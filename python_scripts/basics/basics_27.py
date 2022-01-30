## Print Natural Numbers

print("\n Print 1st 10 Natural Numbers \n")

print("\n------------------------------with for loop-------------------------------------\n")

for i in range(1, 11):
    print(i)

print("\n-----------------------------with while loop------------------------------------\n")

i = 1
while(i <= 10):
    print(i)
    i = i + 1
    
### Remarks:
# * The range(start, stop, step) functuon in python returns a sequence of numbers that starts from 0 by default or the specified start number, increments by default 1 or the specified step number, and stops before the stop number.

print("\n Print 1st 10 Even Numbers \n")

print("\n------------------------------with for loop-------------------------------------\n")

for i in range(1, 11):
    print(2*i)

print("\n-----------------------------with while loop------------------------------------\n")

i = 1
while(i <= 10):
    print(2*i)
    i = i + 1
    
print("\n Print 1st 10 Odd Numbers \n")

print("\n------------------------------with for loop-------------------------------------\n")

for i in range(1, 11):
    print(2*i - 1)

print("\n-----------------------------with while loop------------------------------------\n")

i = 1
while(i <= 10):
    print(2*i - 1)
    i = i + 1
    
print("\n Print Numbers in Reverse Order \n")

maximum = int(input("Please Enter the Maximum integer Value : "))
minimum = int(input("Please Enter the Minimum integer Value : "))

print("List of Natural Numbers from {0} to {1} : ".format(maximum, minimum)) 

while ( maximum >= minimum):
    print (maximum, end = '  ')
    maximum = maximum - 1