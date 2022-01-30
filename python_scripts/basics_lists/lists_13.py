## Difference between two lists

print("\n Difference between two lists\n")

print("\n---------------------------------1. using sets----------------------------------\n")

list1 = [1, 2, 4, 6, 8, 9]
list2 = [1, 3, 5, 7, 11, 9]

print("\nFirst  List Items = ", list1)
print("\nSecond List Items = ", list2)

diff1 = list(set(list1) - set(list2))
diff2 = list(set(list2) - set(list1))
print("\nElements in list 1 and not in list 2", diff1)
print("\nElements in list 2 and not in list 1", diff2)

actualdiff = diff1 + diff2
print("\nList Difference Result = ", actualdiff)

print("\n-------------------------2. using for loop and if ------------------------------\n")

print("\nFirst  List Items = ", list1)
print("\nSecond List Items = ", list2)

List_Difference = []

for val in list1 + list2:
    if val not in list1 or val not in list2:
        List_Difference.append(val)

print("\nList Difference = ", List_Difference)

print("\n---------------------3. using if and list comprehension ------------------------\n")

print("\nFirst  List Items = ", list1)
print("\nSecond List Items = ", list2)

list_diff = [x for x in list1 + list2 if x not in list1 or x not in list2]

print("\nList Difference = ", list_diff)