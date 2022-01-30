# Python numpy mod and remainder function

import numpy as np

print("Python numpy mod and remainder function.\n")

a = np.array([10, 50, 100, 150, 250])
print("Array a",a) 

b = np.array([6, 5, 4, 3, 2])
print("\nArray b of same length as Array a",b)
 
c = np.array([[26,  48,  91,  57, 120], [33,  95,  68, 109, 155], [111, 194,   7,  22, 124], [ 82, 119,  18, 156,  81],[ 38,  10, 151,  24,  14]])
print("\nArray c\n",c) 


d = np.array([[12, 11,  0,  9,  7], [10,  4, 11,  6,  9], [ 9,  2, 10,  9, 11], [ 5, 14,  0, 11,  8], [ 5, 12,  5,  5, 11]])
print("\nArray d of same length as Array c\n",d)

print("\n Mod of  a and 3\n", np.mod(a,3))

print("\n Mod of c and 4\n", np.mod(c,4))

print("\n Mod of  a and b\n", np.mod(a,b))

print("\n Mod of d and c\n", np.mod(d,c))

print("\n-----------------------------------------------------------\n")

print("\n Remainder of  a and 3\n", np.remainder(a,3))

print("\n Remainder of c and 4\n", np.remainder(c,4))

print("\n Remainder of  a and b\n", np.remainder(a,b))

print("\n Remainder of d and c\n", np.remainder(d,c))