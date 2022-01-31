## Matplotlib Line color

# You can use the keyword argument color or the shorter c to set the color of the line:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color = 'r')
plt.show()

# Can use any of the 140 supported color names.

plt.plot(ypoints, c = 'hotpink')
plt.show()
