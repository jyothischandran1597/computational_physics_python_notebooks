# Replace infinity and NaN (Not a Number) values in a Python array

print("Replace infinity and NaN (Not a Number) values in a Python array.\n")

import numpy as np

arr1 = np.array([10, 20, 50, 90, 5, 40, 60, 30, 25], dtype = 'float')
print("\n-----Arr1------\n",arr1)

arr1[2] = np.nan
arr1[4] = np.inf
print("\n-----Arr1 with nan and inf------\n",arr1)

# Replace inf and nan With 11.56
x = np.isinf(arr1) | np.isnan(arr1)
arr1[x] = 11.56
print("\n-----Arr1 with nan and inf replaced with 11.56------\n",arr1)

arr2 = np.array( [[9, 7, np.nan, 8, np.inf],
                  [np.nan, 3, 7, np.inf, 5],
                  [8, np.inf, 4, np.nan, 1]],
                 dtype = 'float')
print("\n-----Arr2------\n")
print( arr2)

# Replace inf and nan in arr2 With 29.16
y = np.isinf(arr2) | np.isnan(arr2)
arr2[y] = 29.16
print("\n-----Arr2 with nan and inf replaced with 29.16------\n",arr2)