## Accessing List Index and Values - Part 1

print("\nAccessing List Index and Values - Part 1\n")

Num_List = [10, 20, 30, 40, 50]

print("\n-----------------------------using for loop-------------------------------------\n")
print("List Index and Values are")
for i in range(len(Num_List)):
    print("Index Number = ", i, " and Value = ", Num_List[i])

    
print("\n-----------------------------using enumerate------------------------------------\n")

    
## REMARK: Using enumerate(iterable, start=0)

#Enumerate is a very useful and convenient function while using loops. One way to loop over a list's index is using range(length_of_list). Instead of using the range() function, we can instead use the built-in enumerate() function in python. enumerate() allows us to iterate through a sequence but it keeps track of both the index and the element.

#Using enumerate is preferred in most cases due to better readability and logic.

print("List Index and Values are")
for index, value in enumerate(num_list):
    print("Index Number = ", index, " and Value = ", value)
    
