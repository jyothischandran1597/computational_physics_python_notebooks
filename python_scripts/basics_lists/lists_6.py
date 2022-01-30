## Accessing List Index and Values - Part 3

print("\nAccessing List Index and Values - Part 3\n")

    
print("\n------------------------using zip, range and len--------------------------------\n")

Num_List = [22, 44, 66, 88, 122]

print("List Index and Values are")
for index, value in zip(range(len(Num_List)), Num_List):
    print("Index Number = ", index, " and Value = ", value)

print("")
print(list(zip(range(len(Num_List)), Num_List)),'\n')