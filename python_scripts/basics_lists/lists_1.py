# Appending items to lists

print("\nAppending items to lists \n")
numbers = [10, 20, 30, 40, 50]

print("\nNumeric List Before Appending Item")
print(numbers)

numbers.append(65)

print("\nNumeric List After Appending First Item")
print(numbers)

value = int(input("\nPlease enter the List Item = "))
numbers.append(value)

print("\nNumeric List After Appending Second Item")
print(numbers)

countries = ["India", "USA", "UK", "Italy"]

print("\nList Before Appending Item")
print(countries)

countries.insert(3, "Japan")
print("\nList After Appending Japan at 3rd Index Position")
print(countries)

countries.insert(0, "China")
print("\nList After Appending China at 0 Index Position")
print(countries)

countries.insert(6, "France")
print("\nList After Appending France at 6 Index Position")
print(countries)

numbers = [11, 22, 33, 44, 55, 66]

print("\nNumeric List Before Inserting Item")
print(numbers)


index = int(input("\nPlease enter Index Position = "))
value = int(input("\nPlease enter the List Value = "))

numbers.insert(index, value)

print("\nNumeric List After Appending Item")
print(numbers)