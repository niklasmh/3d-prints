import numpy as np
from solid import *
from solid.utils import *

z = 0.1
z2 = z * 2
m = 2

t = translate
tx = lambda e, x: t([x, 0, 0])(e)
ty = lambda e, x: t([0, x, 0])(e)
tz = lambda e, x: t([0, 0, x])(e)
txy = lambda e, x, y: t([x, y, 0])(e)
r = rotate
rx = lambda e, x: r([x, 0, 0])(e)
ry = lambda e, x: r([0, x, 0])(e)
rz = lambda e, x: r([0, 0, x])(e)
sc = lambda e, x: scale([x, x, x])(e)
sx = lambda e, x: scale([x, 1, 1])(e)
sy = lambda e, x: scale([1, x, 1])(e)
sxy = lambda e, x: scale([x, x, 1])(e)
sz = lambda e, x: scale([1, 1, x])(e)
cos = np.cos
sin = np.sin
pi = np.pi
save = lambda m, n: scad_render_to_file(m, n, file_header="$fn = 64;")

# Parameters
ri = (19.3 + 0.5) / 2  # Inner radius
ro = ri + 3  # Outer radius
h = 20  # Height


def leg_shape(min=ro, max=ri, steps=32):
    points = []
    for x in np.linspace(0, 1, steps):
        y = x**4 * (max - min)
        points.append([min + y, x * h])
    return points


def create_leg_tip(padding=0):
    slice = tx(circle(r=ro - ri), ri)
    slice += polygon([[ri, 0], *leg_shape(), [ri, h]])
    slice += ty(square([ri, h]), ri - ro)
    slice -= ty(square([ri, h]), padding)
    # return slice
    model = rotate_extrude(segments=32)(slice)
    return model


legs = [
    create_leg_tip(padding=0),
]

for i in range(1, len(legs)):
    legs[i] = tx(legs[i], i * (ro * 2 + m))

model = union()(*legs)

save(model, "marius-leg-fix.scad")
