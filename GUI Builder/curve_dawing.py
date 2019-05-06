import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
N = 100000

theta = np.linspace(-4 * np.pi, 4 * np.pi, N)
R = 10
r = 2
s = 0.4
t = np.linspace(-2, 2, N)

x = (R + r * (np.cos(20 * theta) + s * np.cos(1000 * theta))) * np.cos(theta)
y = (R + r * (np.cos(20 * theta) + s * np.cos(1000 * theta))) * np.sin(theta)
z = 3 * t + (np.sin(20 * theta) + s * np.sin(1000 * theta))
ax.plot(x, y, z, label='parametric curve')
ax.legend()

plt.show()
