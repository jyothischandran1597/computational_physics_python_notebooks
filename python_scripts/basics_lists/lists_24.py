## Find the Second Largest Number in a List

print("\n Find the Second Largest Number in a List\n")

print("\n------------------------1. set(), list.remove() and max()-----------------------\n")

list1 = [10, 20, 4, 45, 99, 99]
print("List Items = ", list1)


list2 = set(list1)
list2.remove(max(list2)) # Note that this is actually a set.
print("The Second Largest Element in this List is : ",max(list2))

print("\n----------------------------2. set() and list()---------------------------------\n")

list1 = [10, 20, 4, 45, 99, 99]

temp_list = list(set(list1))
Num = temp_list[-2]
print("The Second Largest Element in this List is : ",Num)

print("\n----------------------------3. for loop and if---------------------------------\n")

secondLargest = list1[0]
largest = list1[0]
for i in range(len(list1)):
    if list1[i] > largest:
        largest = list1[i]

for i in range(len(list1)):
    if list1[i] > secondLargest and list1[i] != largest:
        secondLargest = list1[i]
        
print("The Second Largest Element in this List is : ",secondLargest)

print("\n----------------------------4. for loop and elif--------------------------------\n")

first = second = list1[0]
for j in range(1, len(list1)):
    if(list1[j] > first):
        second = first
        first = list1[j]
    elif(list1[j] > second and list1[j] < first):
        second = list1[j]
        

print("The Largest Element in this List is : ", first)
print("The Second Largest Element in this List is : ", second)

print("\n-----------------------5.list.sort() and list.reverse()-------------------------\n")

list1 = [10, 20, 4, 45, 99]

list1.sort()
list1.reverse()

print("The Largest Element in this List is : ", list1[1])