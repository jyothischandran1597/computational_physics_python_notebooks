# Accessing 2D numpy array elements using index

import numpy as np

arr = np.array([[1, 2, 3, 4, 5],[12, 15, 61, 11, 19]])

print("The array is ",arr)
print("The shape of the array is ",arr.shape)
print("Value at index (0,1): ",arr[0][1])
print("Value at index (0,4): ",arr[0][4])
print("Value at index (1,1): ",arr[1][1])