## Print Negative Numbers in a Range

### 1. Using for loop

print("\nEven numbers from 1 to n\n")
print("\n------------------------------with for loop and if------------------------------\n")

minimum = int(input("Enter the Minimum Number = "))
maximum = int(input("Enter the Maximum Number = "))

print("\nAll Negative Numbers from {0} and {1}".format(minimum, maximum)) 
for num in range(minimum, maximum + 1):
    if num < 0:
        print(num, end = '   ')
        
print("\n------------------------with for loop and custom function-----------------------\n")
        
def negativeNumbers(x, y):
    for num in range(x, y + 1):
        if num < 0:
            print(num, end = '   ')


minimum = int(input("Enter the Minimum Number = "))
maximum = int(input("Enter the Maximum Number = "))

print("\nAll Negative Numbers from {0} and {1}".format(minimum, maximum)) 
negativeNumbers(minimum, maximum)

### 2. Using while loop
print("\n----------------------------with while loop and if------------------------------\n")

minimum = int(input("Enter the Minimum Number = "))
maximum = int(input("Enter the Maximum Number = "))

print("\nAll Negative Numbers from {0} and {1}".format(minimum, maximum))
num = minimum
while num <= maximum:
    if num < 0:
        print(num, end = '   ')
    num = num + 1