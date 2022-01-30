# Python ndarray dtype

import numpy as np

print("\n-------------------array data types-----------------------\n")
arr1 = np.array([10, 20, 30, 40, 50])
 
print("Array 1          : ", arr1)
print("Data Type : ", arr1.dtype)
 
arr2 = np.array([1, 3.10, 4.60, 5, 7.96])
 
print("\nArray 2        : ", arr2)
print("Data Type : ", arr2.dtype)

list1 = [10, 20, 30, 40, 50]
 
arr3 = np.array(list1, dtype = 'int')
  
print("\nArray 3          : ", arr3)
print("Data Type : ", arr3.dtype)
 
arr4 = np.array(list1, dtype = 'float')
print("\nArray 4           : ", arr4)
print("Data Type : ", arr4.dtype)
 
arr5 = np.array(list1, dtype = 'float16')
print("\nArray 5           : ", arr5)
print("Data Type : ", arr5.dtype)

arr6 = np.array(list1, dtype = 'S')
print("\nArr6           : ", arr6)
print("Arr6 Data Type : ", arr6.dtype)

list2 = [0,1,2,0,5]
arr7 = np.array(list2, dtype = 'bool')
print("\nList to build Arr7: ", list2)
print("Arr7           : ", arr7)
print("Arr7 Data Type : ", arr7.dtype)
 
arr8 = np.array([1, 10, 'e', 'o', 9, 'Hi', 7], dtype = 'object')
print("\nArr8           : ", arr8)
print("Arr8 Data Type : ", arr8.dtype)