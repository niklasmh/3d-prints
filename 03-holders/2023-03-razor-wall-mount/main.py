from sdf import *
import numpy as np
from math import pi

cm = 10  # Centimeters

# Wall mount
WIDTH = 5*cm
HEIGHT = 4*cm
DEPTH = 0.4*cm
RADIUS = WIDTH/16

# Razor holder
RH_GAP = 3.5*cm
RH_WIDTH = 0.7*cm
RH_LENGTH = 3*cm
RH_RADIUS = RH_WIDTH / 2

f = rounded_rectangle(np.array((WIDTH, HEIGHT)), RADIUS)
f = f.extrude(DEPTH)

f = rounded_rectangle(np.array((RH_WIDTH, RH_LENGTH)), RH_RADIUS)
f = f.extrude(DEPTH)
f = f.rotate(pi / 2)
f = f.rotate(pi / 2, X)
f = f.translate((0, -RH_LENGTH, 0))
f = f.wrap_around(0, 0)
f = f & slab(z0=-0.5, z1=0.5, x0=0)

#g = sphere(1)
#f |= g

f.save('razor-wall-mount.stl', step=.2)
