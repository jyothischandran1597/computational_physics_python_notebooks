# 2D Numpy array slicing

import numpy as np

arr2 = np.array([[26, 48, 91, 57, 120], [33, 95, 68, 109, 155],
                [111, 194, 7, 22, 124], [ 82, 119, 18, 156, 81],
                [ 38, 10, 151, 24, 14]])
print("The parent array: ", arr2)

print("\nSliced arr2[0:2, 0:2]: \n",arr2[:2, :2])
print("\nSliced arr2[0:3, 0:end]: \n",arr2[:3, :])
print("\nSliced arr2[:3]: \n",arr2[:3])
print("\nSliced arr2[:,:4]: \n",arr2[:,:4])
