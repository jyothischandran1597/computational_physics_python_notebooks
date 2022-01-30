## Check Number is Divisible by 5 and 11

print("\nCheck Number is Divisible by 5 and 11\n")

number = int(input("Please Enter any Positive Integer : "))

if (number % 5 == 0) and (number % 11 == 0):
    print("Given Number {0} is Divisible by 5 and 11".format(number))
else:
    print("Given Number {0} is Not Divisible by 5 and 11".format(number))
    
### Remarks:
# * The 'and' in the if statement works as a logical and.
# * True and False = False; True and True = True.
# * Similarly, 'or' works as logical or.
