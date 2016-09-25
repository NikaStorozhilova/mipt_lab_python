import numpy as np
import pylab
t = np.arange(0, 2*np.pi, 0.1)
pylab.ion()
for a in np.arange(1, 50, 0.1):
  x = np.sin(t+a)
  y = np.cos(2*t)
  pylab.clf()
  pylab.plot (x, y)
  pylab.draw()
  pylab.pause(0.1)
pylab.close()