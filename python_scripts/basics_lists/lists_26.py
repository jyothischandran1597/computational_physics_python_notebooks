## Left/Right Rotate a List by n

print("\n Left/Right Rotate a List by n\n")

print("\n-------------------------------1. nested for loops------------------------------\n")

List_ = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

Rotate = int(input("\nEnter Position to Left Rotate List Items = "))

print('\nOriginal List Items Before Rotating')
print(List_)

List=List_.copy()
for i in range(Rotate):
    firstValue = List[0]
    for j in range(len(List) - 1):
        List[j] = List[j + 1]
    List[len(ltList) - 1] = firstValue

print('\nFinal List Items After Left Rotating: ')
print(List)

List = List_.copy()
l = len(List)-1
for i in range(Rotate):
    lastValue = List[l]
    for j in range(l, -1 ,-1):
        List[j] = List[j - 1]
    List[0] = lastValue

print('\nFinal List Items After Right Rotating: ')
print(List)

print("\n-------------------------------2. index slicing------------------------------\n")

List = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Rotate = int(input("Enter Position to Rotate List Items = "))

list1 = List[-Rotate:] + List[:-Rotate]
list2 = List[Rotate:] + List[:Rotate]

print('\nFinal List Items After Right Rotating')
print(list1)
print('\nFinal List Items After Left Rotating')
print(list2)