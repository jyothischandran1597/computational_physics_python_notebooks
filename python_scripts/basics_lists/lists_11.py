## Simple operations on Lists - Part 3

print("\n Simple operations on Lists - Part 3\n")

print("\n-----------------------1.1 Add a list: for loop--------------------------------\n")

Sum_List = []

list_length = int(input("Enter the Total List Items = "))
for i in range(1, list_length + 1):
    list_value = int(input("Enter the {} list Item = ".format(i)))
    Sum_List.append(list_value)

print("List Items = ", Sum_List)

list_sum = 0

for i in range(list_length):
    list_sum = list_sum + Sum_List[i]
    
print("The Sum of all the List Items = ", list_sum)

print("\n--------------------1.2 Add a list: sum() function--------------------------\n")

list_sum_1=sum(Sum_List)

print("The Muliplication of all the List Items using sum func = ", list_sum_1)

print("\n-----------------------2.1 Multiply a list: for loop----------------------------\n")

multiList = []

listNumber = int(input("Enter the Total List Items = "))
for i in range(1, listNumber + 1):
    listValue = int(input("Enter the {} List Item = ".format(i)))
    multiList.append(listValue)

print("\nList Items = ", multiList)

listMulti = 1

for num in multiList:
    listMulti = listMulti * num

print("\nThe Muliplication of all the List Items = ", listMulti)

print("\n--------------------2.2 Add a list: while loop--------------------------\n")

print("\nList Items = ", multiList)

listMultiplication = 1
i = 0

while (i < listNumber):
    listMultiplication = listMultiplication * multiList[i]
    i = i + 1
    
print("\nThe Multiplication of all the List Items = ", listMultiplication)

print("\n--------------------1.2 Add a list: function def--------------------------\n")

def listMultiplication(multiList):
    listMulti = 1

    for num in multiList:
        listMulti = listMulti * num
    return listMulti

print("\nList Items = ", multiList)

listMultip = listMultiplication(multiList)

print("\nThe Multiplication of all the List Items = ", listMultip)