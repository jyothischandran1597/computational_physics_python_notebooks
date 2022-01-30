## Print Even and Odd Numbers in a List

print("\n Print Even and Odd Numbers in a List\n")

print("\n------------------------------1. for loop and if-------------------------------\n")

NumList = [1,2,3,4,5,6,7,8,9,10]
Number = len(NumList)

print("\nParent List: ",NumList)

print("\nEven Numbers in this List are : ")
for j in range(Number):
    if(NumList[j] % 2 == 0):
        print(NumList[j], end = '   ')
        
print("\nOdd Numbers in this List are : ")
for j in range(Number):
    if(NumList[j] % 2 != 0):
        print(NumList[j], end = '   ')
        
print("\n-----------------------------2. while loop and if-------------------------------\n")

print("\nEven Numbers in this List are : ")
j=0
while(j < Number):
    if(NumList[j] % 2 == 0):
        print(NumList[j], end = '   ')
    j = j + 1
    
i=0
print("\nOdd Numbers in this List are : ")
while(i < Number):
    if(NumList[i] % 2 != 0):
        print(NumList[i], end = '   ')
    i = i + 1
    
print("\n-----------------------------3. custom function-------------------------------\n")

def even_numbers(NumList):
    for j in range(Number):
        if(NumList[j] % 2 == 0):
            print(NumList[j], end = '   ')
            
def odd_numbers(NumList):
    for j in range(Number):
        if(NumList[j] % 2 != 0):
            print(NumList[j], end = '   ')

            
print("\nEven Numbers in this List are : ")
even_numbers(NumList)

print("\nOdd Numbers in this List are : ")
odd_numbers(NumList)