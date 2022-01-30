## Sum of two numbers

number1 = input("Enter the first number: ")
number2 = input("Enter the secod number: ")

# Using arithmetic + Operator to add two numbers

sum_ = float(number1) + float(number2)
print('The sum of {0} and {1} is {2}'.format(number1, number2, sum_))

### Remarks:
#* A method in python is a function that ia attached to an object.
#* .format() is a method that helps us to insert value of variables into a string.
#* The function float(number) used here converts any type of number inserted into a floating point number, or a number with a decimal point.

number1 = float(input("Please Enter the First Number: "))
number2 = float(input("Please Enter the Second number: "))

# Using arithmetic + Operator to add two numbers
sum_ = number1 + number2
print('The sum of {0} and {1} is {2}'.format(number1, number2, sum_))

sub = number1 - number2
print('The Result of subtracting {0} from {1} = {2}'.format(number2,number1,sub))