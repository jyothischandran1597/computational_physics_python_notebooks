# Python Numpy random array
import numpy as np

print("Python Numpy random array")

np.random.seed(100)
# The seed forces the random numbers to be same every time. Otherwise they will be different eavery time.

print(np.random.random(5),'\n')
print(np.random.random((4, 4)),'\n')
print(np.random.random((2, 3, 4)),'\n')