# Create an array from existing array

import numpy as np

print("Create an array from existing array\n")

arr1 = np.array([10, 50, 100, 150, 250])
arr2 = np.array([[26, 48, 91, 57, 120], [33, 95, 68, 109, 155],
                [111, 194, 7, 22, 124], [ 82, 119, 18, 156, 81],
                [ 38, 10, 151, 24, 14]])

print("\nArray1 \n",arr1)
print("\nArray2 \n",arr2)

arr3 = arr1[2:7]
print("\nArray3 = Array1[2:7] \n",arr3)

arr4 = arr1[3:]
print("\nArray4 = Array1[3:] \n",arr4)

arr5 = arr2[::-1,]
print("\nArray5 = Array2[::-1,] \n",arr5)

arr6 = arr2[::-1, ::-1]
print("\nArray6 = Array2[::-1, ::-1] \n",arr6)