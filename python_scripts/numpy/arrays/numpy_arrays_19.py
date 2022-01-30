# Slicing Numpy ndarray with Negative Values

print("Slicing Numpy ndarray with Negative Values.\n")

import numpy as np

arr1 = np.array([10, 25, 50, 75, 100, 125, 150, 200, 250])
arr2 = np.array([[26, 48, 91, 57, 120], [33, 95, 68, 109, 155],
                [111, 194, 7, 22, 124], [ 82, 119, 18, 156, 81],
                [ 38, 10, 151, 24, 14]])

print("\n Parent array 1: \n", arr1)

print("\n The slice [0:3]:\n", arr1[:3])
print("\n The slice [0:end-4]:\n", arr1[:-4])
print("\n The slice [end-4:end]:\n", arr1[-4:])

print("\n Parent array 2: \n", arr1)

print("\n The slice [:-2, :-1:\n", arr2[:-2, :-1])
print("\n The slice [:-3, :-1]:\n", arr2[:-3, :-1])
print("\n The slice [:,:-3]:\n", arr2[:,:-3])
print("\n The slice [:,:-2]:\n", arr2[:,:-2])
                                        