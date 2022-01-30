## Accessing List Index and Values - Part 2

print("\nAccessing List Index and Values - Part 2\n")

    
print("\n------------------------using list comprehension--------------------------------\n")

### List Comprehension

# List comprehensions are used for creating new lists from other iterables like tuples, strings, arrays, lists, etc. A list comprehension consists of brackets containing the expression, which is executed for each element along with the for loop to iterate over each element. 

## New_List = [ expression(element) for element in Old_List if condition ] 

# List comprehensions are a more time and space efficient option with better readability when we have to modify elements of a list or operate on elements of an interable.


Num_list = [13, 43, 56, 78, 65]

list_1 = [list((i, Num_list[i])) for i in range(len(Num_list))]
print("List Index and Values as lists are")
print(list2)

list_2 = [(i, Num_list[i]) for i in range(len(Num_list))]
print("List Index and Values as tuples are")
print(list3)

list_3 = [(index, value) for index, value in enumerate(Num_List)]
print("List Index and Values defined as tuples using enumerate are")
print(list3)