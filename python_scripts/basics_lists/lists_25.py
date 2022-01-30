## Sort List Items in Descending Order

print("\n Sort List Items in Descending Order\n")

print("\n------------------------1. list.sort() and list.reverse()-----------------------\n")

int_list = [5,4,9,7,3,1,6,8,2]
print("\nInitial List: ", int_list)

int_list.sort()
int_list.reverse()

print('\nList Items After Sorting in Descending Order')
print(int_list)

print("\n------------------------2. nested for and temp variables-----------------------\n")

intlist = [5,4,9,7,3,1,6,8,2]

for i in range(len(intlist)):
    for j in range(i + 1, len(intlist)):
        if(intlist[i] < intlist[j]):
            temp = intlist[i]
            intlist[i] = intlist[j]
            intlist[j] = temp
    
print('List Items After Sorting in Descending Order\n',intlist)

print("\n-----------------------3. nested while and temp variables-----------------------\n")

intlist = [5,4,9,7,3,1,6,8,2]

i = 0
while(i < len(intlist)):
    j = i + 1
    while j < len(intlist):
        if(intlist[i] < intlist[j]):
            temp = intlist[i]
            intlist[i] = intlist[j]
            intlist[j] = temp
        j = j + 1
    i = i + 1
    
print('List Items After Sorting in Descending Order\n',intlist)