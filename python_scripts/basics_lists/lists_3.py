## List length

print("\nList length \n")

List = [1,2,3,4,5,6,7,8,9]

print("\nThe length of the List", List," is ", len(List))

stringList = ['Krishna', 'John', 'Yung', 'Ram', 'Steve']

print("\nThe length of the", stringList," List is ", len(stringList))

mixedList = ['Krishna', 20, 'John', 40.5, 'Yung', 11.98, 'Ram', 22]
print("\nThe mixed list is: ",mixedList)
print("\nThe length of the mixed list List is ", len(mixedList))

mixedList2 = ['Krishna', 20, 'John', (40, 50, 65), 'Yung', 11.98, 'Ram']
print("\nThe mixed list is: ",mixedList2)
print("\nThe length of the 2nd mixed List is ", len(mixedList2),'\n')

nested_List = ['Krishna', 20, 'John', [20, 40, 50, 65, 22], 'Yung', 11.98]
print("\nThe nested list is: ",nested_List)
print("\nLength of the nested list is ",len(nested_List))
print("\nLength of the inner list is ",len(nested_List[3]),'\n')