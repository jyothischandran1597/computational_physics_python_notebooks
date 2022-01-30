## Print List Items at Even Position

print("\n Print List Items at Even Position\n")

print("\n-------------------------------1. index slicing----------------------------\n")

List = [3, 6, 9, 11, 13, 15, 17, 19]
print("\nParent List: ",List)
length = len(List)

print('\nPrinting the List Items at Even Position:\n',List[1:length:2])

print("\n-------------------------------2. for loop----------------------------\n")

print('Printing the List Items at Even Position')
for i in range(1, length, 2):
    print(List[i], end = '  ')
    
print("\n-------------------------------3. while loop----------------------------\n")

print('Printing the List Items at Even Position')
i = 1
while i < len(List):
    print(List[i], end = '  ')
    i = i + 2
    
print("\n-------------------------------4. for loop and if----------------------------\n")

print('\nPrinting the List Items at Even Position')
for i in range(length):
    if i % 2 != 0:
        print(List[i], end = '  ')