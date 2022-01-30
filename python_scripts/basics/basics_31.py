## Find Distance Between Two Points

print("\n Find Distance Between Two Points \n")

import math

x1 = int(input("Enter the First Point Coordinate x1  = "))
y1 = int(input("Enter the First Point Coordinate y1  = "))
x2 = int(input("Enter the Second Point Coordinate x2 = "))
y2 = int(input("Enter the Second Point Coordinate y2 = "))


x = math.pow((x2 - x1), 2)
y = math.pow((y2 - y1), 2)

print("x2 - x1 = ",x)
print("y2 - y1 = ",y)
distance = math.sqrt(x + y)

print('The Distance Between Two Points = {} Units'.format(distance))

print("\n-------------------------with a custom function---------------------------------\n")

def distanceBetweenTwo(x1, y1, x2, y2):
    return math.sqrt((math.pow((x2 - x1), 2)) + (math.pow((y2 - y1), 2)))


x1 = int(input("Enter the First Point Coordinate x1  = "))
y1 = int(input("Enter the First Point Coordinate y1  = "))
x2 = int(input("Enter the Second Point Coordinate x2 = "))
y2 = int(input("Enter the Second Point Coordinate y2 = "))

distance = distanceBetweenTwo(x1, y1, x2, y2)

print('The Distance Between Two Points = {0} Units'.format(distance))