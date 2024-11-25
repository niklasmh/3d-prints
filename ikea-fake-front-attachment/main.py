from solid import *
from solid.utils import *

mm = 1

width = 45*mm + 1.8*mm
height = 41*mm - 3.5*mm
padding = 25*mm
thickness = 1.7*mm
wall_spacing = 3*mm # (stem width - front corner edge spacing) / 2 = (562mm - 556mm) / 2 = 3mm
m = 2*mm


def screw_hole(x, y):
    screw = z(cylinder(d=5.1*mm, h=20*mm))
    screw_hat = z(cylinder(d=9*mm, h=20*mm))
    screw_hat = translate([0, 0, 2*mm])(screw_hat)
    return translate([x, y, 0])(screw + screw_hat)


def attachment():
    blank = cube([width + 2*m + padding, height + 2*m, wall_spacing + thickness + m])
    blank = translate([-padding/2, 0, 0])(blank)

    corner_part = z(cube([width, height, thickness]))
    corner_part = translate([m, 0, wall_spacing])(corner_part)

    o = 2 * m
    r = width / 2 - o
    a = z(cube([width - 2*o, height - r - o + m, m]))
    a = translate([m + o, 0, wall_spacing + thickness])(a)
    b = z(cylinder(r, m))
    b = translate([width / 2 + m, height - r - o + m, wall_spacing + thickness])(b)
    look_through_window = a + b

    hole_spacing = 32*mm
    hole_depth = 27*mm
    hole_position = width / 2 + m - hole_spacing
    screw_holes = [
        screw_hole(hole_position, hole_depth),
        screw_hole(hole_position + hole_spacing, hole_depth),
        screw_hole(hole_position + 2*hole_spacing, hole_depth),
    ]

    part = blank - corner_part - look_through_window - screw_holes
    part = rotate([90, 0, 0])(part)

    return part


def z(part):
    """ Avoid z-fighting on basic shapes """
    t = 0.001
    s = 1.001
    part = scale([s, s, s])(part)
    part = translate([-t, -t, -t])(part)
    return part


fn = 32
scad_render_to_file(attachment(), "ikea-fake-front-attachment.scad",
                    file_header='$fn = %d;' % fn)
