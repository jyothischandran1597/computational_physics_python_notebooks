## Simple operations on Lists - Part 2

print("\n Simple operations on Lists - Part 2\n")


NumList1 = [10, 20, 30]
NumList2 = [5, 2, 3]

print("\n Lists to be operated are: \n",NumList1," and ",NumList2)

add = []
sub = []
multi = []
div = []
mod = []
expo = []
 
for j in range(len(NumList1)):
    add.append( NumList1[j] + NumList2[j])
    sub.append( NumList1[j] - NumList2[j])
    multi.append( NumList1[j] * NumList2[j])
    div.append( NumList1[j] / NumList2[j])
    mod.append( NumList1[j] % NumList2[j])
    expo.append( NumList1[j] ** NumList2[j])
 
print("\nThe List Items after Addition =  ", add)
print("The List Items after Subtraction =  ", sub)
print("The List Items after Multiplication =  ", multi)
print("The List Items after Division =  ", div)
print("The List Items after Modulus =  ", mod)
print("The List Items after Exponent =  ", expo,'\n')

print("\n----------------------- Using input to get lists--------------------------------\n")


NumList1 = []; NumList2 = []
add = [] ; sub = [] ; multi = []
div = []; mod = [] ; expo = []
i = 0
j = 0
Number = int(input("Please enter the Total Number of List Elements: "))
print("Please enter the Items of a First and Second List   ")
while(i < Number):
    List1value = int(input("Please enter the {} Element of List1 : ".format(i)))
    NumList1.append(List1value)

    List2value = int(input("Please enter the {} Element of List1 : ".format(i)))
    NumList2.append(List2value)
    i = i + 1
    
while(j < Number):
    add.append( NumList1[j] + NumList2[j])
    sub.append( NumList1[j] - NumList2[j])
    multi.append( NumList1[j] * NumList2[j])
    div.append( NumList1[j] / NumList2[j])
    mod.append( NumList1[j] % NumList2[j])
    expo.append( NumList1[j] ** NumList2[j])
    j = j + 1
 
print("\nThe List Items after Addition =  ", add)
print("The List Items after Subtraction =  ", sub)
print("The List Items after Multiplication =  ", multi)
print("The List Items after Division =  ", div)
print("The List Items after Modulus =  ", mod)
print("The List Items after Exponent =  ", expo)