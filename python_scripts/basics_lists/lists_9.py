## Simple operations on Lists - Part 1

print("\n Simple operations on Lists - Part 1\n")

print("\n-----------------------1. Add 2 lists: for loop--------------------------------\n")

Num_List_1 = [10, 20, 30]
Num_List_2 = [15, 25, 35]
total = []
 
for j in range(3):
    total.append( Num_List_1[j] + Num_List_2[j])
 
print("\nThe total Sum of Two Lists =  ", total)

print("\n--------------------2. Add 2 lists:list comprehension--------------------------\n")

total = [num_1 + num_2 for num_1, num_2 in list(zip(Num_List_1,Num_List_2))]

print("\nThe total Sum of Two Lists using list comprehension=  ", total)

# Just adding the two lists with + will result in a joined list (Num_List_1 + Num_List_2)

print("\n------------------------3. Add 2 lists: while loop-----------------------------\n")

NumList1 = []
NumList2 = []
total = []
i = 1
j = 0

Number = int(input("Please enter the Total Number of List Elements: "))
print("Please enter the Items of a First and Second List   ")
while(i <= Number):
    List1value = int(input("Please enter the {} Element of List1 : ".format(i)))
    NumList1.append(List1value)

    List2value = int(input("Please enter the {} Element of List2 : ".format(i)))
    NumList2.append(List2value)
    i = i + 1
    
while(j < Number):
    total.append( NumList1[j] + NumList2[j])
    j = j + 1
 
print("\nThe total Sum of Two Lists =  ", total)
