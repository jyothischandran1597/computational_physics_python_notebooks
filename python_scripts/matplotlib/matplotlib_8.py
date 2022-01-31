## Matplotlib Line style

# You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line.

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()

plt.plot(ypoints, linestyle = 'dashed')
plt.show()

# The line style can be written in a shorter syntax:

# linestyle can be written as ls.

# dotted can be written as :.

# dashed can be written as --.

plt.plot(ypoints, ls = ':')
plt.show()