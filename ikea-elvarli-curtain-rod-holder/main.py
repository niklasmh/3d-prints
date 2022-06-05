from solid import *
from solid.utils import *
from math import *

# Constants
cm = 10
z = 0.01  # Fix z-fighting
z2 = 2*z
fn = 32  # Circle details

# Physical measurements
h = 6.0*cm  # Height of this thing
e_w = 5.55*cm  # Elvarli post width
e_d = 2.6*cm  # Elvarli post depth
i_w = 1.0*cm  # Indent width
i_d = 0.7*cm  # Indent depth
r_r = 1.45*cm  # Rod radius

# Parameters
p = 0.5*cm  # Padding around this thing
p2 = 2*p
r_p = 0.5*cm  # Rod holder padding
r_th = 0.8*cm  # Rod holder tip height
r_tr = r_p / 2 + 0.1*cm  # Rod holder tip radius


def generate_attachment_base():
    attachment = cube([e_w + p2, e_d + p2, h])
    attachment = translate([-p, -p, z])(attachment)
    attachment_hole = cube([e_w, e_d, h + z2])
    attachment -= attachment_hole

    attachment_indent = cube([i_w, i_d, h])
    attachment_indent_front = translate(
        [e_w / 2 - i_w / 2, 0, 0])(attachment_indent)
    attachment_indent_back = translate(
        [e_w / 2 - i_w / 2, e_d - i_d, 0])(attachment_indent)

    attachment += attachment_indent_front
    attachment += attachment_indent_back

    return attachment


def generate_rod_holder():
    holder = cylinder(r_r + r_p, e_d + p2)
    holder = rotate([90])(holder)
    holder = translate([e_w + p + r_r, e_d + p - z, h - r_r - r_p])(holder)

    angle = 42 / 180 * pi
    u_x, u_y = sin(angle), cos(angle)
    x, y = r_r + (r_r + r_p) * u_x, h - (r_r + r_p + (r_r + r_p) * u_y)
    support = linear_extrude(
        e_d + p2)(polygon([[0, 0], [0, h - r_r - r_p], [x, y]]))
    support = rotate([90])(support)
    support = translate([e_w + p, e_d + p - z])(support)
    holder += support

    holder_hole = cylinder(r_r, e_d + p2 + z2)
    holder_hole = rotate([90])(holder_hole)
    holder_hole = translate(
        [e_w + p + r_r, e_d + p, h - r_r - r_p])(holder_hole)
    holder -= holder_hole

    holder_top_cut = cube([(r_r + r_p) * 2, e_d + p2 + z2, h - r_r])
    holder_top_cut = translate([e_w, -p - z2, h - r_r - r_p])(holder_top_cut)
    holder -= holder_top_cut

    tip = cube([r_p, e_d + p2, r_th])
    tip = translate([e_w + p + r_r * 2, -p, h - r_r - r_p])(tip)
    holder += tip

    bevel_edge = cylinder(r_tr, e_d + p2 + z2, segments=16)
    bevel_edge = rotate([90])(bevel_edge)
    bevel_edge = translate(
        [e_w + p + r_r * 2 + r_p - r_tr, e_d + p, h - r_r - r_p + r_th])(bevel_edge)
    holder += bevel_edge

    return holder


model = generate_attachment_base() + generate_rod_holder()

scad_render_to_file(model, "ikea-elvarli-curtain-rod-holder.scad",
                    file_header=f"$fn = {fn};")
