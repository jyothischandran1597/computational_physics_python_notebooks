## Sum of 10 Numbers Until a Negative Number is entered

print("\n Sum of 10 Numbers Until a Negative Number is entered \n")
print("\n------------------------------with for loop-------------------------------------\n")

Sum = 0

print("Please Enter 10 Numbers\n")
for i in range(1, 11):
    num = int(input("Number {:d} = ".format(i)))

    if num < 0:
        break

    Sum = Sum + num

print("The Sum of Positive Numbers = ", Sum)

print("\n------------------------------with while loop-----------------------------------\n")

Sum = 0

print("Please Enter 10 Numbers\n")
i = 1
while(i <= 10):
    num = int(input("Number {:d} = ".format(i)))

    if num < 0:
        break

    Sum = Sum + num
    i = i + 1

print("The Sum of Positive Numbers = ", Sum)