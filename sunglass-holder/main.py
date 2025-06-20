import numpy as np
from solid import *
from solid.utils import *
import json

z = 0.1
z2 = z*2
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
save = lambda m, n: scad_render_to_file(m, n, file_header='$fn = 64;')

# Parameters
hook_gap = 60    # Gap between the hooks
hook_count = 4   # Number of hooks along the rod
hook_radius = 28  # Radius of the hooks
hook_offset = -0.55 # Offset for the hooks
hook_points = json.load(open("extracted_points.json", "r"))

rod_length = hook_gap * hook_count  # Length of the rod
rod_height = 15  # Height of the rod
rod_depth = 3    # Depth of the rod

dist_from_wall = 15  # Distance from the wall to the rod


def create_hook():
    points = np.array(hook_points)
    points[-1][1] = points[0][1]
    points *= np.array([1, -1]) * 2

    min_x = np.min(points[:, 0])
    max_x = np.max(points[:, 0])
    max_y = np.max(points[:, 1])

    margin = 0.2
    hook_shape = polygon(
        points=[
            [min_x, max_y + margin],
            *points,
            [max_x, max_y + margin],
        ]
    )

    hook = linear_extrude(height=rod_depth)(hook_shape)

    hook = ty(hook, -points[0][1])
    hook = sxy(hook, -1 / (max_x - min_x))
    hook = sx(hook, -1)
    hook = tx(hook, hook_offset)

    hole = cube([1, 1, rod_depth + z2])
    hole = txy(hole, hook_offset, -margin)
    hole = tz(hole, -z)

    return hook, hole


def create_rod():
    rod = cube([rod_length, rod_height, rod_depth])

    for i in range(hook_count):
        x = (i + 0.5) * hook_gap
        hook, hole = create_hook()
        hook = sxy(hook, hook_radius * 2)
        hole = sxy(hole, hook_radius * 2)
        hook = txy(hook, x, rod_height)
        hole = txy(hole, x, rod_height)
        rod -= hole
        rod += hook

    wall_mount = cylinder(r=rod_height / 2, h=rod_depth + dist_from_wall)
    wall_mount = ty(wall_mount, rod_height / 2)

    n = 6
    for i in range(n):
        wall_mount += multmatrix(
            [
                [1, 0, 0, 0],
                [0, 1, i / n / 2, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ]
        )(wall_mount)

    rod += wall_mount
    for i in range(hook_count):
        rod += tx(wall_mount, (i + 1) * hook_gap)

    return rod


def sunglass_holder():
    return create_rod()


save(sunglass_holder(), "sunglass-holder.scad")
