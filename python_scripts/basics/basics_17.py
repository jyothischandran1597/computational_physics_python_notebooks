## Print Divisors of a Number

### 1. Using for loop


print("\nEven numbers from 1 to n\n")
print("\n------------------------------with for loop and if------------------------------\n")


num = int(input("Please enter any integer to find divisors = "))

print("The Divisors of the Number = ")

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end='  ')
        
print("\n----------------------with for loop and custom function-------------------------\n")

def findDivisors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end='  ')

num = int(input("Please enter any integer to find divisors = "))

print("The Divisors of the Number = ")
findDivisors(num)

### 1. Using while loop

print("\n------------------------------with while loop and if----------------------------\n")

num = int(input("Please enter any integer to find divisors = "))

print("The Divisors of the Number = ")

i = 1

while(i <= num):
    if num % i == 0:
        print(i, end = '  ')
    i = i + 1
