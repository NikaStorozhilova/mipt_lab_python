import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10, 0.0001)
y = 0
for n in np.arange(0, 50, 1):
    y += 0.5**n*np.cos(3**n*np.pi*x)
plt.plot(x, y)
plt.show()