## Read 10 Numbers and Find their Sum and Average

### Remarks:
# * for loop and while loop are the two types of loops that are used commonly. For loop runs repeatedly over a set of iterable values and while loop runs till a specific condition is met.
# * While loop is slower than for loop in most cases as it includes additional steps of checkin the truth of a statment and modifying the variable that is checked in each loop.
# * As long as we  know the number of times the iterating step is to be performed, python convention is to rely more on for loop.
# * At the same time, if we only know a condition for the termination of the itereating step, we use the while loop.

print("\n Sum and Average of 10 numbers \n")
print("\n------------------------------with for loop-------------------------------------\n")


Sum = 0

print("Please Enter 10 Numbers\n")
for i in range(1, 11):
    num = int(input("Number {} = ".format(i)))
    Sum = Sum + num

avg = Sum / 10#..............Normal division
floor_avg = Sum // 10#.......Division to the next lowest integer.

print("The Sum of 10 Numbers     = ", Sum)
print("The Average of 10 Numbers = ", avg)
print("The Floor Average of 10 Numbers = ", floor_avg)

print("\n------------------------------with while loop-----------------------------------\n")

Sum = 0

print("Please Enter 10 Numbers\n")
i = 1
while(i <= 10):
    num = int(input("Number{} = ".format(i)))
    Sum = Sum + num
    i = i + 1

avg = Sum / 10
floor_avg = Sum // 10

print("The Sum of 10 Numbers     = ", Sum)
print("The Average of 10 Numbers = ", avg)
print("The Floor Average of 10 Numbers = ", floor_avg)