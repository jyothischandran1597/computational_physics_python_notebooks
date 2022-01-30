# Numpy Array Transpose

print("Numpy Array Transpose.\n")

import numpy as np
 
a = np.array([[26, 48, 91, 57, 120], [33, 95, 68, 109, 155],
             [111, 194, 7, 22, 124], [ 82, 119, 18, 156, 81],
             [ 38, 10, 151, 24, 14]])
 
b = np.array([[12, 11, 0, 9, 7], [10, 4, 11, 6, 9],
             [ 9, 2, 10, 9, 11], [ 5, 14, 0, 11, 8]])
 
print('Original')
print(a)
print('\nTransposed ')
print(a.T)
 
print('\nOriginal')
print(b)
print('\nTransposed')
print(np.transpose(b))