## Cube of  number

# Python Program to Calculate Cube of a Number

number = float(input(" Please Enter any numeric Value : "))
cube = number * number * number
print("The Cube of a Given Number {0} by multiplication = {1}".format(number, cube))

# Using exponent operator

cube = number ** 3
print("The Cube of a Given Number {0} using exponent operator = {1}".format(number, cube))

# Python Program to Calculate Cube of a Number by defining a function.

def cube(num):
    return num * num * num

cub = cube(number)
print("The Cube of a Given Number {0} by defining a function = {1}".format(number, cub))

# ### Remarks:
# * In the above example, a function is defined that will calculate the cube of a number and called to do so.
# * The function name and the parameters it takes in as inputs are given after starting the definition of the function using "def".
# * When the function is called later in the script, it will return the value of the statement that is given after the word "return".