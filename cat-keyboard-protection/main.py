import numpy as np
from solid import *
from solid.utils import *

z = 0.01
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
sc = scale
sx = lambda e, x: sc([x, 1, 1])(e)
sy = lambda e, x: sc([1, x, 1])(e)
sz = lambda e, x: sc([1, 1, x])(e)
cos = np.cos
sin = np.sin
pi = np.pi
save = lambda m, n: scad_render_to_file(m, n, file_header='$fn = 64;')

# Parameters
keyboard_width = 269      # Width of the keyboard cover
keyboard_depth = 101      # Depth of the keyboard cover
keyboard_thickness = 2    # Key height
support_lines = [
    27.5,
    45.75,
    64,
    82.5,
]
support_thickness = 1.5   # Thickness of the support lines

touchpad_width = 133      # Width of the touchpad cover
touchpad_depth = 89       # Depth of the touchpad cover
touchpad_margin = 0.5  # Touchpad indentation height

cover_thickness = 2       # Thickness of the keyboard cover
cover_margin = 4          # Margin around the keyboard and touchpad covers


def create_keyboard_cover():
    base = cube([
        keyboard_width + cover_margin,
        keyboard_depth + cover_margin,
        cover_thickness + keyboard_thickness
    ])

    hole = cube([
        keyboard_width,
        keyboard_depth,
        keyboard_thickness + z2
    ])
    hole = txy(hole, cover_margin / 2, cover_margin / 2)
    hole = tz(hole, cover_thickness)

    support = []
    for y in support_lines:
        line = cube([keyboard_width, support_thickness, keyboard_thickness + z])
        line = txy(line, cover_margin / 2, y - support_thickness / 2 + cover_margin / 2)
        line = tz(line, cover_thickness)
        support.append(line)

    cover = base - hole + support

    return cover


def create_touchpad_cover():
    base = cube([
        touchpad_width + cover_margin * 3,
        touchpad_depth + cover_margin * 3,
        cover_thickness + touchpad_margin * 2
    ])

    hole = cube([
        touchpad_width - cover_margin,
        touchpad_depth - cover_margin,
        touchpad_margin * 2 + cover_thickness
    ])
    hole = txy(hole, cover_margin * 2, cover_margin * 2)
    hole = tz(hole, cover_thickness)

    cover = base - hole

    return cover


save(create_keyboard_cover(), "cat-keyboard-protection.keyboard.scad")
save(create_touchpad_cover(), "cat-keyboard-protection.touchpad.scad")
