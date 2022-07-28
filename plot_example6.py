import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

np.random.seed(42)
ages = np.random.randint(low = 8, high = 30, size=35)
heights = np.random.randint(130, 195, 35)
weights = np.random.randint(30, 160, 35)
bmi = weights / ((heights * 0.01)**2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs = heights, ys = weights, zs = ages, s=bmi*5 )
ax.set_title("Age-wise body weight-height distribution")
ax.set_xlabel("Height (cm)")
ax.set_ylabel("Weight (kg)")
ax.set_zlabel("Age (years)")
plt.show()