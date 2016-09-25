 import math
  import pylab
  from matplotlib import mlab

  xmin = -20.0
  xmax = 20.0

  dx = 0.01
  xlist = mlab.frange (xmin, xmax, dx)

  pylab.ion()

  for n in range (50):
          ylist = [math.cos(2*x) for x in xlist]
  pylab.clf()
  pylab.plot (xlist, ylist)
  pylab.draw()
pylab.pause(0.3)


  pylab.close()