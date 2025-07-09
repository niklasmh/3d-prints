import numpy as np
from solid import *
from solid.utils import *

z = 0.01
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
sc = scale
sx = lambda e, x: sc([x, 1, 1])(e)
sy = lambda e, x: sc([1, x, 1])(e)
sz = lambda e, x: sc([1, 1, x])(e)
cos = np.cos
sin = np.sin
pi = np.pi
save = lambda m, n: scad_render_to_file(m, n, file_header="$fn = 64;")

# Parameters
ro_adapter = 26.8 / 2
ri_adapter = 22.2 / 2
h_adapter = 11.1
circ_adapter = 2 * pi * ro_adapter

count_adapter_bumps = 8
gap_adapter_bumps = 3.3
r_adapter_bump = (circ_adapter / count_adapter_bumps - gap_adapter_bumps) / 2

r_hole_adapter = 8.2 / 2
h_hole_adapter = 5.2
d_hole_adapter = 11.1


def create_adapter():
    adapter = cylinder(r=ro_adapter, h=h_adapter)

    bumps = []
    for i in range(count_adapter_bumps):
        angle = i * (2 * pi / count_adapter_bumps)
        x = ro_adapter * cos(angle)
        y = ro_adapter * sin(angle)
        bump = txy(cylinder(r=r_adapter_bump, h=h_adapter + z2), x, y)
        bump = tz(bump, -z)
        bumps.append(bump)

    adapter -= bumps

    hole = cylinder(r=r_hole_adapter, h=d_hole_adapter + z2)
    hole *= tz(
        cube([r_hole_adapter * 2, h_hole_adapter, d_hole_adapter + z2], center=True),
        d_hole_adapter / 2 + z,
    )
    hole = tz(hole, -z)

    adapter -= hole

    return adapter


save(create_adapter(), "aqara-roller-shade.adapter.scad")
