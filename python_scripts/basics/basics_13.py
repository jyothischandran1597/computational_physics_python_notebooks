### Even numbers from 1 to n 

print("\nEven numbers from 1 to n\n")
print("\n------------------------------with for loop and if------------------------------\n")

maximum = int(input("Please Enter the Maximum Value : "))

for number in range(1, maximum+1):
    if(number % 2 == 0):
        print(number)
        
print("\n------------------------------with for loop alone-------------------------------\n")

for number in range(2, maximum+1, 2):
    print(number)
    
print("\n------------------------------with for while and if-----------------------------\n")

maximum = int(input("Please Enter the Maximum Value : "))

number = 1

while number <= maximum:
    if(number % 2 == 0):
        print(number)
    number = number + 1