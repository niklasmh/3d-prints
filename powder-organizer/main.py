import numpy as np
from solid import *
from solid.utils import *

z = 0.01
z2 = z * 2
m = 1.5

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
w_cup = 1.5
r_bottom = 4
ri_cup = 43 / 2
ro_cup = ri_cup + w_cup
h_cup = 40


def create_cup():
    # Outer shape
    o_shape = square([ro_cup, h_cup])
    o_shape -= txy(square([r_bottom, r_bottom]), ro_cup - r_bottom + z, -z)
    o_shape += txy(circle(r=r_bottom, segments=16), ro_cup - r_bottom, r_bottom)

    # Inner shape
    i_shape = txy(square([ri_cup, h_cup]), -z, w_cup)
    i_shape -= txy(square([r_bottom, r_bottom]), ro_cup - r_bottom + z, -z)
    i_shape += txy(circle(r=r_bottom - w_cup, segments=16), ro_cup - r_bottom, r_bottom)

    shape = o_shape - i_shape

    # Smooth top corner
    r = 1
    shape += txy(circle(r=w_cup * r), ro_cup + w_cup * (r - 1), h_cup)
    angle = 30
    x = sin(angle * pi / 180) * w_cup * r * 2
    y = -cos(angle * pi / 180) * w_cup * r * 2
    shape += txy(
        square([w_cup * r, w_cup * r]), ro_cup + w_cup * (r - 2.5) + x, h_cup + y
    )
    shape -= txy(circle(r=w_cup * r), ro_cup + w_cup * (r - 1) + x, h_cup + y)

    # Create model
    model = rotate_extrude(angle=360)(shape)

    # Create mask
    s = (ro_cup + m) / ro_cup
    mask = tz(sc(s)(rotate_extrude(angle=360)(o_shape)), -m)

    return model, mask


cup, cup_mask = create_cup()
save(cup, "powder-organizer.cup.scad")


def create_organizer(cup_mask):
    mask = cup_mask
    model = cylinder(h=h_cup, r=ro_cup * 3 + m * 10, segments=12)
    model = rz(model, 15)

    for i in np.linspace(0, 360, 6, endpoint=False):
        r = ro_cup * 2 + m * 6
        x = cos(i * pi / 180) * r
        y = sin(i * pi / 180) * r
        mask += txy(cup_mask, x, y)
        model += txy(cylinder(h=h_cup, r=ro_cup + m * 7.5, segments=64), x, y)

    model = tz(model, -m * 3)
    s = ro_cup / (ro_cup + m / 2)
    model -= tz(sc(s)(model), h_cup * 0.6)

    return model - mask


def create_organizer(cup_mask):
    mask = cup_mask
    h = h_cup + m * 2
    model = cylinder(h=h, r=ro_cup * 3 + m * 13.5, segments=6)

    for i in np.linspace(0, 360, 6, endpoint=False):
        r = ro_cup * 2 + m * 6
        x = cos(i * pi / 180) * r
        y = sin(i * pi / 180) * r
        x2 = cos((i + 30) * pi / 180) * r * 2.0
        y2 = sin((i + 30) * pi / 180) * r * 2.0
        mask += txy(cup_mask, x, y)
        model += txy(cylinder(h=h, r=ro_cup + m * 7.5, segments=64), x, y)
        model -= tz(
            txy(cylinder(h=h + z2 * 10, r=ro_cup + m * 7.5, segments=64), x2, y2),
            -z * 10,
        )

    model = tz(model, -m * 3)
    s = ro_cup / (ro_cup + m / 2)
    hole = tz(sc(s)(model), h * 0.6)
    ms = m * 2 / h_cup
    bottom_track = tz(sx(sy(sz(model, ms), s), s), -m * 3.5)

    return model + bottom_track - mask - hole, model


organizer, organizer_mask = create_organizer(cup_mask)
save(organizer, "powder-organizer.organizer.scad")


def create_lid(organizer_mask):
    hs = m * 2 / h_cup
    model = sz(organizer_mask, hs)
    s = ro_cup / (ro_cup + m / 2 * 1.2)
    model += tz(sz(sy(sx(organizer_mask, s), s), hs), m * 1.5)
    s = ro_cup / (ro_cup + m / 2 * 0.8)
    model -= tz(sz(sy(sx(organizer_mask, s), s), hs), -m * 1.5)

    indent = tz(cylinder(h=m * 3, r=ro_cup + 1 + m, segments=64), m)
    extra = tz(cylinder(h=m * 2.4, r=ri_cup - 0.2, segments=64), m)
    model -= indent
    model += extra

    for i in np.linspace(0, 360, 6, endpoint=False):
        r = ro_cup * 2 + m * 6
        x = cos(i * pi / 180) * r
        y = sin(i * pi / 180) * r
        model -= txy(indent, x, y)
        model += txy(extra, x, y)

    return model


lid = create_lid(organizer_mask)
save(lid, "powder-organizer.lid.scad")
