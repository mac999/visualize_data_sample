import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

np.random.seed(42)
xs = np.random.random(100)*10 + 20
ys = np.random.random(100)*5 + 7
zs = np.random.random(100)*15 + 50

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs,ys,zs)

plt.show()