## matplotlib Bar Chart - 3


from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
sns.set()

x = np.array(["A", "B", "C", "D", "E", "F", "G", "H"])
y = np.array([3, 8, 1, 10, 6, 5, 9, 7])


plt.bar(x, y, width=0.4, color = ['r','g','b','y'], hatch = ("O"))
plt.show()


