# Numpy multiply function and * operator)

import numpy as np

print("Array addition using numpy Arithmetic Operator +\n")

a = np.array([10, 50, 100, 150, 250])
print("Array a",a) 

b = np.array([6, 5, 4, 3, 2])
print("\nArray b of same length as Array a",b)
 
c = np.array([[26,  48,  91,  57, 120], [33,  95,  68, 109, 155], [111, 194,   7,  22, 124], [ 82, 119,  18, 156,  81],[ 38,  10, 151,  24,  14]])
print("\nArray c\n",c) 

d = np.array([[12, 11,  0,  9,  7], [10,  4, 11,  6,  9], [ 9,  2, 10,  9, 11], [ 5, 14,  0, 11,  8], [ 5, 12,  5,  5, 11]])
print("\nArray d of same length as Array c\n",d)

print("\n Multiply a and b\n", np.multiply(a, b))

print("\n Multiply c and d\n", np.multiply(c, d))

print("\n Multiply a and c (different dim.)\n", np.multiply(a, c))

print("\n Multiply a, b and c (different dim.)\n", np.multiply(a, b,c))

print("\n-----------------------------------------------------------\n")
print("Array multiplication using numpy Arithmetic Operator *\n")

a = np.array([10, 50, 100, 150, 250])

b = np.array([6, 5, 4, 3, 2])
 
c = np.array([[26,  48,  91,  57, 120], [33,  95,  68, 109, 155], [111, 194,   7,  22, 124], [ 82, 119,  18, 156,  81],[ 38,  10, 151,  24,  14]])

d = np.array([[12, 11,  0,  9,  7], [10,  4, 11,  6,  9], [ 9,  2, 10,  9, 11], [ 5, 14,  0, 11,  8], [ 5, 12,  5,  5, 11]])

print("\n Multiply a and b\n", a*b)

print("\n Multiply c and d\n", c*d)

print("\n Multiply a and c (different dim.)\n", a*c)

print("\n Multiply a, b and c (different dim.)\n", a*b*c)

print("\n Multiply a, b, c and d (different dim.)\n", a*b*c*d)
