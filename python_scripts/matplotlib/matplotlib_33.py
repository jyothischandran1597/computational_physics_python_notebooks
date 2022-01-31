## 3-D Plotting

import numpy as np
import matplotlib.pyplot as plt
 
fig = plt.figure(1)
 
# syntax for 3-D projection
ax = plt.axes(projection ='3d')
 
# defining all 3 axes
z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)
 
# plotting
ax.plot3D(x, y, z, 'green')
ax.set_title('3D line plot')
plt.show()

fig = plt.figure(2)
 
# syntax for 3-D projection
ax = plt.axes(projection ='3d')
 
# defining axes
z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)
c = x + y
ax.scatter(x, y, z, c = c)
 
# syntax for plotting
ax.set_title('3d Scatter plot')
plt.show()