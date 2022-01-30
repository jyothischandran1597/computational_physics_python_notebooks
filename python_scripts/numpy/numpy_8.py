# Python numpy zeros array

'''
The Python Numpy zeros function creates an array of zeros. This 
function accepts the arguments to specify the shape. For example,

    zeros(2) means a one-dimensional of two zero elements.
    zeros(2, 3) means 2 * 3 matrix of zeros.
    and zeros(2, 3, 4) means a three-dimensional of zeros.
'''

import numpy as np

print("Python array of zeros from numpy.zeros()\n")
print(np.zeros(3), '\n Dimensions:', np.zeros(3).shape, '\n')
print(np.zeros((2, 2)), '\n Dimensions:', np.zeros((2,2)).shape, '\n')

print(np.zeros((2, 3)), '\n Dimensions:', np.zeros((2,2)).shape, '\n')
print(np.zeros((4, 7)), '\n Dimensions:', np.zeros((4,7)).shape, '\n')
print(np.zeros((3, 2, 7)), '\n Dimensions:', np.zeros((3,2,7)).shape, '\n')