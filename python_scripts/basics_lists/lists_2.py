## Extend a List

# list.extend(iterator)

print("\nExtend a List \n")

countries = ["India", "USA", "UK", "Italy"]

print("List before appending item")
print(countries)

tuple1 = ("Japan", "China", "France")
countries.extend(tuple1)
print("\nList after appending Tuple using extend")
print(countries)

list1 = [19, 17, 39, 55]
countries.extend(list1)
print("\nList after appending List using extend")
print(countries)

countries.extend((11.5, 19.2))
print("\nList after appending numbers using extend")
print(countries)