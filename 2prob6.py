import numpy as np
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6]
y = [1, 1.42, 1.76, 2, 2.24, 2.5]
p = np.polyfit(x, y, deg = 1)
p_f = np.poly1d(p)
t = np.arange(0, 10.01,0.01)
plt.plot(t, p_f(t))
plt.errorbar(x, y, xerr=0.05, yerr=0.1)
p = np.polyfit(x, y, deg = 2)
p_f = np.poly1d(p)
plt.grid(True)
plt.show()