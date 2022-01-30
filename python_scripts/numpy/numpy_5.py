# Multi-dimensional arrays

import numpy as np

two_arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("2-d array:\n", two_arr)
print("The dimensions are: ", two_arr.shape)

matrix = np.array([[1, 2, 3], [10, 20, 30], [6, 7, 8]])
print("\n3*3 matrix in form of  an array:\n", matrix)
print("The dimensions are: ", matrix.shape)

three_array = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("\n3-d array:\n", three_array)
print("The dimensions are: ", three_array.shape)