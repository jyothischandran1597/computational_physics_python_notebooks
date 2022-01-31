## Matplotlib scatterplot - 2 Color and marker

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(5, 50, 50)

y = np.random.randint(100, 1000, 50)

fix, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize = (8, 4))

ax1.scatter(x, y, marker = '+', color = 'red')
ax2.scatter(x, y, marker = '^', color = 'blue')
ax3.scatter(x, y, marker = '$\clubsuit$', color = 'green',
            alpha = 0.5)

plt.show()

# The Matplotlib module has a number of available colormaps.

# A colormap is like a list of colors, where each color has a value that ranges from 0 to 100.

# You can specify the colormap with the keyword argument cmap with the value of the colormap, in this case 'viridis' which is one of the built-in colormaps available in Matplotlib.

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.colorbar()

plt.show() 


