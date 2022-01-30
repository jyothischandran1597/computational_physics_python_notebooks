# Python numpy array from lists

import numpy as np
 
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
 
print("A 1-D array object defined using numpy: ",arr)

a = [1, 2, 3, 4, 5]
arr1 = np.array(a)
print("A 1-D array object defined from a list: ", arr1)

b = [2.5, 3.5, 7, 4.5, 8]
arr2 = np.array(b)
print("A 1-D array object defined from a list: ", arr2)