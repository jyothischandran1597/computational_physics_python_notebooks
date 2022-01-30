## Count Even and Odd Numbers in a list

print("\n Count Even and Odd Numbers in a list\n")

print("\n--------------------------------1. Using for loop-------------------------------\n")

NumList = [1,2,3,4,5,6,7,8,9]
print("\nList    = ", NumList)

Even_count = 0
Odd_count = 0

for j in range(len(NumList)):
    if(NumList[j] % 2 == 0):
        Even_count = Even_count + 1
    else:
        Odd_count = Odd_count + 1

print("\nTotal Number of Even Numbers in this List =  ", Even_count)
print("Total Number of Odd Numbers in this List =  ", Odd_count)

print("\n------------------------------2. Using while loop-------------------------------\n")

Even_count = 0
Odd_count = 0
j = 0
Number = len(NumList)

while(j < Number):
    if(NumList[j] % 2 == 0):
        Even_count = Even_count + 1
    else:
        Odd_count = Odd_count + 1
    j = j + 1

print("\nTotal Number of Even Numbers in this List =  ", Even_count)
print("Total Number of Odd Numbers in this List = ", Odd_count)

print("\n------------------------------2. Using function-------------------------------\n")

def count_even(NumList):
    Even_count = 0
    for j in range(Number):
        if(NumList[j] % 2 == 0):
            Even_count = Even_count + 1
    return Even_count

def count_odd(NumList):
    Odd_count = 0
    for j in range(Number):
        if(NumList[j] % 2 != 0):
            Odd_count = Odd_count + 1
    return Odd_count

even_count = count_even(NumList)
odd_count = count_odd(NumList)
print("\nTotal Number of Even Numbers in this List =  ", even_count)
print("Total Number of Odd Numbers in this List = ", odd_count)