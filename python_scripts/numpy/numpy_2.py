# Python numpy array from a list of lists

import numpy as np

print("Python Numpy ndarray from a list of lists")
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('List of Lists = ', a)
print()
 
arr = np.array(a)
print(arr)