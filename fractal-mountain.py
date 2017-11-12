import numpy, random
from mayavi import mlab

levels = 11
size = 2 ** (levels - 1)
height  = numpy.zeros((size + 1, size + 1))

for lev in range(levels):
  step = size // 2 ** lev
  for y in range(0, size + 1, step):
    jumpover = 1 - (y // step) % 2 if lev > 0 else 0
    for x in range(step * jumpover, size + 1, step * (1 + jumpover)):
      pointer = 1 - (x // step) % 2 + 2 * jumpover if lev > 0 else 3
      yref, xref = step * (1 - pointer // 2), step * (1 - pointer % 2)
      corner1 = height[y - yref, x - xref]
      corner2 = height[y + yref, x + xref]
      average = (corner1 + corner2) / 2.0
      variation = step * (random.random() - 0.5)
      height[y,x] = average + variation if lev > 0 else 0

xg, yg = numpy.mgrid[-1:1:1j*size,-1:1:1j*size]
surf = mlab.surf(xg, yg, height, colormap='gist_earth', warp_scale='auto')
mlab.show()

