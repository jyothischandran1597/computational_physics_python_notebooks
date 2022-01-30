## Plotting Without Line

# To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.title("Plot x vs y as points")
plt.show()