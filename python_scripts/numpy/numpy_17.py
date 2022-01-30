# 1D Numpy array slicing

import numpy as np

arr1 = np.array([10, 25, 50, 75, 100, 125, 150, 200, 250])
print("The parent array: ", arr1)

print("Sliced array[1:5]: ",arr1[1:5])
print("Sliced array[3:end]: ",arr1[3:])
print("Sliced array[0:7]: ",arr1[:7])

