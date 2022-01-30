## Find Sum and Average of N natural numbers

print("\n Find Sum and Average of N natural numbers \n")
print("\n------------------------------with for loop ------------------------------------\n")

number = int(input("Please Enter any Number: "))
total = 0

for value in range(1, number + 1):
    total = total + value

average = total / number

print("The Sum of Natural Numbers from 1 to {0} =  {1}".format(number, total))
print("Average of Natural Numbers from 1 to {0} =  {1}".format(number, average))

print("\n------------------------------with while loop ----------------------------------\n")

number = int(input("Please Enter any Number: "))

total = 0
value = 1

while (value <= number):
    total = total + value
    value = value + 1

average = total / number

print("The Sum of Natural Numbers from 1 to {0} =  {1}".format(number, total))
print("Average of Natural Numbers from 1 to {0} =  {1}".format(number, average))

print("\n------------------------------with custom function------------------------------\n")

def sum_and_avg_of_natural_numbers(num):
    if(num == 0):
        return num
    else:
        return (num * (num + 1) / 2)
    
number = int(input("Please Enter any Number: "))

total = sum_and_avg_of_natural_numbers(number)
average = total / number

print("The Sum of Natural Numbers from 1 to {0} =  {1}".format(number, total))
print("Average of Natural Numbers from 1 to {0} =  {1}".format(number, average))