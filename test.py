import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

V_0 = 1
a = 1
x = np.linspace(0.001,1,999)
y = np.linspace(0.001,1,999)
x,y = np.meshgrid(x,y)


V = 2*V_0/np.pi*np.arctan(np.sin(np.pi*y/a)/np.sinh(np.pi*x/a))


fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x,y,V)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('V/V_0')
plt.show()