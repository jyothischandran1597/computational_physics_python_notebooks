## Clone or Copy a List

print("\n Clone or Copy a List\n")

print("\n--------------------------------1. Using list()--------------------------------\n")

orgList = [10, 20, 30, 40, 50, 60, 70]
print("\nOriginal List Items    = ", orgList)
print("\nOriginal List Datatype = ", type(orgList))

newList = list(orgList)
print("\nNew List Items    = ", newList)
print("\nNew List Datatype = ", type(newList))

print("\n-----------------------------2. Using list.copy()------------------------------\n")

newList = orgList.copy()
print("\nNew List Items      = ", newList)

print("\n-----------------------------3. Using index slicing-----------------------------\n")

newList = orgList[:]
print("\nNew List Items      = ", newList)

print("\n-----------------------------4. Using list.extend()-----------------------------\n")

newList = []
newList.extend(orgList)
print("\nNew List Items      = ", newList)

print("\n--------------------------5. Using list comprehension---------------------------\n")

newList = [lVal for lVal in orgList]
print("\nNew List Items      = ", newList)

print("\n--------------------------6. Using for loop and append()------------------------\n")

newList = []

for lVal in orgList:
    newList.append(lVal)
print("\nNew List Items      = ", newList)