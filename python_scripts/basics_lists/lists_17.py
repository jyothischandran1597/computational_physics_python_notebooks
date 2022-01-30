## Find Largest and Smallest Number in a List

print("\n Count Even and Odd Numbers in a list\n")

print("\n--------------------------------1. max() and min()------------------------------\n")

a = [10, 50, 60, 120, 20, 15]

print("The Largest Element in this List is : ", max(a))
print("The Smallest Element in this List is : ", min(a))

print("\n---------------------------------2. sort()--------------------------------------\n")

# Python sort function sort the List elements in ascending order.

a = [10, 50, 60, 120, 20, 15]

a.sort()
print("The Largest Element in this List is a[5]: ", a[5])
print("The Largest Element in this List is a[-1]: ", a[-1])
print("The Largest Element in this List is a[len(a)-1]: ", a[len(a)-1])
print("The Smallest Element in this List is : ", a[0])

print("\n-----------------------------3. sort() & reverse()------------------------------\n")

a = [10, 50, 60, 120, 20, 15]

a.sort()
a.reverse()

print("\nThe Largest Element in this List is : ", a[0])
print("The Smallest Element in this List is : ", a[-1])

print("\n--------------------------4. enumerate and if statement-------------------------\n")

a = [10, 50, 60, 120, 20, 15]

largest = a[0]  
smallest = a[0]
for j,value in enumerate(a[1:]):
    if(smallest > value):
        smallest = value
        min_position = j
    if(largest < value):
        largest = value
        max_position = j+1

print("The Smallest Element in this List is : ", smallest)
print("The Index position of Smallest Element in this List is : ", min_position)
print("The Largest Element in this List is : ", largest)
print("The Index position of the Largest Element is : ", max_position)

print("\n--------------------------5. for loop and if statement-------------------------\n")

a = [10, 50, 60, 120, 20, 15]

largest = a[0]  
smallest = a[0]
for j in range(1, len(a)):
    if(smallest > a[j]):
        smallest = a[j]
        min_position = j
    if(largest < a[j]):
        largest = a[j]
        max_position = j


print("The Smallest Element in this List is : ", smallest)
print("The Index position of Smallest Element in this List is : ", min_position)
print("The Largest Element in this List is : ", largest)
print("The Index position of the Largest Element is : ", max_position)