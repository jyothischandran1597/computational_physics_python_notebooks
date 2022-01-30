# Alter array items

import numpy as np

a = np.array([10, 20, 30, 40, 50])
print("The array before altering ",a,'\n')

a[0] = 150
print("The array after altering 0th element as 150",a,'\n')

b = np.array([[10, 50, 100], [250, 500, 1000]])
print("The 2d array before altering\n ",b,'\n')

b[0, 0] = 99
b[1, 1] = 222
b[1, 2] = 444
print("The array after altering b[0, 0] = 99, b[1, 1] = 222 and b[1, 2] = 444: \n",b)
