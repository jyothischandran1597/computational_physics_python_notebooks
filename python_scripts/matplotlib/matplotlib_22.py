## Matplotlib scatterplot - 4 Legends

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)


fig, ax = plt.subplots()
markers = ['o','$\heartsuit$', '$\clubsuit$']
colors = ['tab:blue', 'tab:orange', 'tab:green']
for i,color in enumerate(colors):
    n = 750
    x, y = np.random.rand(2, n)
    scale = 200.0 * np.random.rand(n)
    ax.scatter(x, y, c=color, s=scale, label=color,marker = markers[i],
               alpha=0.6, edgecolors='none', linewidths = 5)

ax.legend()
ax.grid(True)

plt.show()
