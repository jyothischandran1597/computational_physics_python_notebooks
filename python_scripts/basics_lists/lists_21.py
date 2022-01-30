## Put Even and Odd numbers in Separate Lists

print("\n Put Even and Odd numbers in Separate Lists\n")

print("\n------------------------------1. for loop and if-------------------------------\n")

NumList = [1,2,3,4,5,6,7,8,9,10]
Number = len(NumList)

print("\nParent List: ",NumList)

Even = []
Odd = []

for j in range(Number):
    if(NumList[j] % 2 == 0):
        Even.append(NumList[j])
    else:
        Odd.append(NumList[j])

print("Element in Even List is : ", Even)
print("Element in Odd List is : ", Odd)
        
print("\n-----------------------------2. while loop and if-------------------------------\n")

Even = []
Odd = []
j = 0

while(j < Number):
    if(NumList[j] % 2 == 0):
        Even.append(NumList[j])
    else:
        Odd.append(NumList[j])
    j = j + 1

print("Element in Even List is : ", Even)
print("Element in Odd List is : ", Odd)
    
print("\n-----------------------------3. custom function-------------------------------\n")

def even_numbers(NumList):
    Even = []
    for j in range(Number):
        if(NumList[j] % 2 == 0):
            Even.append(NumList[j])

    print("Element in Even List is : ", Even)

def odd_numbers(NumList):
    Odd = []
    for j in range(Number):
        if(NumList[j] % 2 != 0):
            Odd.append(NumList[j])

    print("Element in Odd List is : ", Odd)
      
even_numbers(NumList)
odd_numbers(NumList)