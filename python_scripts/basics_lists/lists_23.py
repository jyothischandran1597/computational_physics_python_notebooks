## Remove Even Numbers in a List

print("\n Remove Even Numbers from List\n")

print("\n-----------------------------1. for & list.remove()-----------------------------\n")

evenList = [11, 22, 31, 44, 51, 65, 71, 82, 91]
print("List Items = ", evenList)

for ev in evenList:
    if (ev % 2 == 0):
        evenList.remove(ev)
    
print("\nList Items after removing even Items = ", evenList)

print("\n----------------------------2. while & list.remove()---------------------------\n")

evenList = [11, 22, 31, 44, 51, 65, 71, 82, 91]
i = 0

while (i < len(evenList)):
    if (evenList[i] % 2 == 0):
        evenList.remove(evenList[i])
    i = i + 1
    
print("List Items after removing even Items = ", evenList)

print("\n-----------------------3. list comprehension & list.remove()--------------------\n")

evenList = [11, 22, 31, 44, 51, 65, 71, 82, 91]
evenList = [ev for ev in evenList if ev % 2 != 0]    
print("List Items after removing even Items = ", evenList)

print("\n---------------------4. list(), filter() and lambda function--------------------\n")

# The filter(function, sequence) method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

evenList = [11, 22, 31, 44, 51, 65, 71, 82, 91]

oddList = list(filter(lambda x : (x % 2 != 0), evenList))    
print("List Items after removing even Items = ", oddList)