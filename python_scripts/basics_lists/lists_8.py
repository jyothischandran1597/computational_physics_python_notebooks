## Reverse a list

print("\nReverse a list\n")

NumList = [1,2,3,4,5,6,7,8,9]
print("\n The List to be Reversed is:\n",NumList)

print("\n---------------------------using list.reverse()---------------------------------\n")

NumList.reverse()#...this permanently changes the list a itself.
print("\nThe Result of a Reverse List =  ", NumList)

print("\n----------------------------using while loop------------------------------------\n")

NumList = [1,2,3,4,5,6,7,8,9]

Number = len(NumList)

j = Number - 1
i = 0

while(i < j):
    temp = NumList[i]
    NumList[i] = NumList[j]
    NumList[j] = temp
    i = i + 1
    j = j - 1
    
print("The Result =  ", NumList)

print("\n--------------------------using function def 1----------------------------------\n")

def reverseList(NumList):
    num = len(NumList)
    j = Number - 1
    i = 0
    while(i < j):
        temp = NumList[i]
        NumList[i] = NumList[j]
        NumList[j] = temp
        i = i + 1
        j = j - 1
        
NumList = [1,2,3,4,5,6,7,8,9]
reverseList(NumList)
print("\nThe Result =  ", NumList)

print("\n--------------------------using function def 2----------------------------------\n")

def reverseList(NumList):
    num = len(NumList)
    rev_list=[]
    i = 0
    while(i < num):
        rev_list.append(NumList[num-i-1])
        i = i + 1
    return rev_list
        
NumList = [1,2,3,4,5,6,7,8,9]
Reverse_List = reverseList(NumList)
print("\nThe Result =  ", Reverse_List)

print("\n---------------------Using function recursively (NEW)---------------------------\n")

def reverseList(NumList, i, j):
    if(i < j):
        temp = NumList[i]
        NumList[i] = NumList[j]
        NumList[j] = temp
        reverseList(NumList, i + 1, j-1)
        
reverseList(NumList, 0, Number - 1)
print("\nThe Result =  ", NumList)