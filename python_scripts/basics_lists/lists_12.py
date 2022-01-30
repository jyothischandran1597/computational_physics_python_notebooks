## Average of List Items

print("\n Average of List Items\n")

print("\n----------------------------------1. for loop-----------------------------------\n")

avglist = []
Number = int(input("Total Number of List Items = "))

for i in range(1, Number + 1):
    value = int(input("Please enter the %d List Item = "  %i))
    avglist.append(value)

total = sum(avglist)
avg = total / Number

print('\nThe Sum Of List Items     = ', total)
print('\nThe Average Of List Items = ', avg)

print("\n---------------------------2. statistics.mean()---------------------------------\n")

from statistics import mean

avglist = []
Number = int(input("Total Number of List Items = "))

for i in range(1, Number + 1):
    value = int(input("Please enter the %d List Item = "  %i))
    avglist.append(value)

total = sum(avglist)
avg = mean(avglist)

print('\nThe Sum Of List Items     = ', total)
print('\nThe Average Of List Items = ', avg)

print("\n-------------------3. functools.reduce() and lambda function--------------------\n")

## Remarks 
### 1. lambda function:

#     lambda~~arguments:~~expression

#Python Lambda Functions are anonymous function means that the function is without a name. As we already know that the def keyword is used to define a normal function in Python. Similarly, the lambda keyword is used to define an anonymous function in Python. Lambda functions are syntactically restricted to a single expression.

#Example:

#    def cube(y):
#        return y*y*y
 
#    lambda_cube = lambda y: y*y*y
    
#    cube(5) == lambda_cube(5)
    
### 2. reduce()

# The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.
# * At first step, first two elements of sequence are picked and the result is obtained.
# * Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
# * This process continues till no more elements are left in the container.
# * The final returned result is returned and printed on console.

avglist = []
Number = int(input("Total Number of List Items = "))

for i in range(1, Number + 1):
    value = int(input("Please enter the %d List Item = "  %i))
    avglist.append(value)

total = sum(avglist)
avg = reduce(lambda x, y: x + y, avglist) / Number
#avg = reduce(lambda x, y: x + y, avglist) /len(avglist)

print('\nThe Sum Of List Items     = ', total)
print('\nThe Average Of List Items = ', avg)
