## Print elements in reverse order

print("\nPrint elements in reverse order\n")

a = [10, 20, 30, 40, 50, 60]
print("\n The List to be Reversed is:\n",a)

print("\n-----------------------------using slicing--------------------------------------\n")


print('Printing the List Items in Rererse:')
print(a[::-1])#...index slicing a[from:end:step]

print("\n---------------------------using list.reverse()---------------------------------\n")

a.reverse()#...this permanently changes the list a itself.
print('\nPrinting the List Items in Reverse\n',a)

print("\n-----------------------------using for loop-------------------------------------\n")

a = [10, 20, 30, 40, 50, 60]

print('\nPrinting the List Items in Reverse\n')
for i in range(len(a)-1, -1, -1):
    print(a[i], end = '  ')
    
print("\n----------------------------using while loop------------------------------------\n")

print('\nPrinting the List Items in Reverse\n')
i = len(a) - 1
while i >= 0:
    print(a[i], end = '  ')
    i = i - 1