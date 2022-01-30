# Boolean index in numpy arrays

# You can use this boolean index to check whether each item in an array with a condition.

print("Boolean index in numpy arrays.\n You can use this boolean index to check whether each item in an array with a condition.\n")

import numpy as np

arr1 = np.array([10, 20, 50, 90, 5, 40, 60, 30, 25])
x = arr1 > 40
print("\nThe array\n",arr1)
print("\nBool index : ", x)
print("\n Array after implementing boolean indexing for array > 40\n", arr1[x])
 
y = arr1 < 40
print("\nBool index : ", y)
print("\n Array after implementing boolean indexing for array < 40\n",arr1[y])
 
arr2 = np.array(np.random.randint(1, 10, size = (3, 8)))
z = arr2 > 4 
print("\n-----Arr2------\n", arr2)
print("------Bool index z------\n", z)
print("------Arr2 of Z------\n", arr2[z])