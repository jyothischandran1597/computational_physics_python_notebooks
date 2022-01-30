## Format Strings for specigying marker, line style and color

# You can use also use the shortcut string notation parameter to specify the marker.

#This parameter is also called fmt, and is written with this syntax:

# marker|line|color
# '*-g' means points marked as *, line is continuous '-' and color is green.

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()