## Sum of 10 Numbers and Skip Negative Numbers

print("\n Sum of 10 Numbers and Skip Negative Numbers \n")
print("\n------------------------------with for loop-------------------------------------\n")

positive_sum = 0

print("Please Enter 10 Numbers to Find Positive Sum\n")
for i in range(1, 11):
    num = int(input("Number {:d} = ".format(i)))

    if num < 0:
        continue

    positive_sum = positive_sum + num

print("The Sum of 10 Numbers by Skipping Negative Numbers = ", positive_sum)

print("\n------------------------------with while loop-----------------------------------\n")

positive_sum = 0

print("Please Enter 10 Numbers to Find Positive Sum\n")
i = 1
while(i <= 10):
    num = int(input("Number {:d} = ".format(i)))

    if num < 0:
        i = i + 1
        continue

    positive_sum = positive_sum + num
    i = i + 1

print("The Sum of 10 Numbers by Skipping Negative Numbers = ", positive_sum)