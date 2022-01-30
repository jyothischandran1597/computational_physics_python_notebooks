## Largest of Three Numbers 

### 1. Using Elif Statement

print("\nPython Program to find Largest of Three Numbers.\n")
print("\n------------------------------elif statements-----------------------------------\n")
 

a = float(input("Please Enter the First value: "))
b = float(input("Please Enter the First value: "))
c = float(input("Please Enter the First value: "))

if (a > b and a > c):
          print("{0} is Greater Than both {1} and {2}". format(a, b, c))
elif (b > a and b > c):
          print("{0} is Greater Than both {1} and {2}". format(b, a, c))
elif (c > a and c > b):
          print("{0} is Greater Than both {1} and {2}". format(c, a, b))
else:
          print("Either any two values or all the three values are equal")

print("\n------------------------------nested if statements------------------------------\n")

a = float(input("Please Enter the First value: "))
b = float(input("Please Enter the First value: "))
c = float(input("Please Enter the First value: "))

if (a-b > 0) and (a-c > 0):
    print("{0} is Greater Than both {1} and {2}". format(a, b, c))
else:
    if (a==b) or (a==c):
        print("Either any two values or all the three values are equal")
    else:
        if(b - c > 0):
            print("{0} is Greater Than both {1} and {2}". format(b, a, c))
        else:
            if b==c:
                print("Either any two values or all the three values are equal")
            else:
                print("{0} is Greater Than both {1} and {2}". format(c, a, b))
    

