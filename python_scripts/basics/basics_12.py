## Odd or Even

print("\nTo determine a number odd or even.\n")

number = int(input("\nPlease Enter any Integer Value : "))

if(number % 2 == 0):
    print("\n{0} is an Even Number".format(number))
else:
    print("\n{0} is an Odd Number".format(number))
    
print("\n-----------------Using the if else statement in a single line------------------\n")

print("{0} is an Even Number".format(number)) if(number % 2 == 0) else print("{0} is an Odd Number\n".format(number))