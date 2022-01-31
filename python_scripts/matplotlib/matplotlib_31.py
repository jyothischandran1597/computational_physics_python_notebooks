# Matplotlib Histogram - 3

# The Python pyplot has a hist2d function to draw a two dimensional or 2D. And to draw matplotlib 2D hist, you need two numerical arrays or array-like values.

import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(10000)

y = 2 * np.random.randn(10000)

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.hist2d(x, y, bins = (10, 10))

ax2.hist2d(x, y, bins = (200, 200))
plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.hist2d(x, y, bins = (10, 10), cmap = 'cubehelix')

ax2.hist2d(x, y, bins = (200, 200), cmap = 'rainbow')
plt.show()