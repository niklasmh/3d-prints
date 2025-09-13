import numpy as np
from solid import *
from solid.utils import *
import json

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
height = 100
thickness = 1.5
i_width = 188.9
o_width = i_width + thickness * 2

lid_depth = 5
lid_notch_position = 3
lid_notch_depth = 1.1
lid_notch_height = 1
lid_notch_width = 7


# Data
shape_points = json.load(open("extracted_points.json", "r"))


def create_extension():
    points = np.array(shape_points)
    points[-1][1] = points[0][1]
    points *= np.array([1, -1]) * 2
    min_x = np.min(points[:, 0])
    max_x = np.max(points[:, 0])

    # Create 2D shape
    shape_polygon = polygon(
        points=[
            *points,
        ]
    )

    # Extrude
    shape = linear_extrude(height=1)(shape_polygon)

    # Center and normalize
    shape = ty(shape, -points[0][1])
    shape = sxy(shape, 1 / (max_x - min_x))
    shape = txy(shape, -0.5, 0.5)

    # Attempt to create symmetry
    shape += sx(shape, -1)
    shape += sy(shape, -1)
    # shape += rz(shape, 90)

    # Adjust size
    i_wall = sxy(shape, i_width)
    i_wall = sz(i_wall, lid_depth)
    o_wall = sxy(shape, o_width)
    o_wall = sz(o_wall, height)

    # Position walls
    i_wall = tz(i_wall, height)

    # Hollow out
    bottom_hole = sz(sxy(shape, i_width - thickness), height + lid_depth + z2)
    body_hole = sz(sxy(shape, i_width), height - thickness)
    body_hole = tz(body_hole, -z)
    hole = bottom_hole + body_hole

    # Create lid notch
    notch = cube([lid_notch_depth * 1.5, lid_notch_width, lid_notch_height])
    notch = tx(notch, -i_width / 2 - lid_notch_depth)
    notch = ty(notch, -lid_notch_width / 2)
    notch += rz(notch, 180)
    bottom_notch = tz(notch, height + lid_notch_position)

    # Subtract notch from top lid
    top_notch = sy(sz(notch, 1.3), 1.4)
    top_notch = tz(top_notch, lid_notch_position * 0.9)

    return i_wall + o_wall - hole + bottom_notch - top_notch


save(create_extension(), "cat-feeder-extension.scad")
