from solid import *
from solid.utils import *
from math import *

# Constants
cm = 10
z = 0.01  # Fix z-fighting
z2 = 2*z
fn = 64  # Circle details

# Physical measurements

# Side (x/y)
# +--center_width--+--roof_support_margin_x--x
# |
# wall_support_margin_z
# |
# z
center_width = 1.5*cm
roof_support_margin_x = 1.5*cm
wall_support_margin_z = 1.5*cm

# Front (z/y)
# +--support_margin_y--+--center_depth--+--support_margin_y--y
#                               |
#                      wall_support_margin_z
#                               |
#                               z
center_depth = 3*cm
support_margin_y = 1.5*cm * 0

width = center_width + roof_support_margin_x
depth = support_margin_y + center_depth + support_margin_y
height = wall_support_margin_z
m = 0.2*cm

# Light strip
ls_width = 1.15*cm
ls_depth = 1.2*cm
ls_height = 0.4*cm
ls_indent_width = 0.15*cm
ls_indent_height = 0.2*cm


def generate_light_strip_holder():
    holder = cube([ls_width + m, ls_depth,
                  ls_height + ls_indent_height])
    cutout = cube([ls_width + z2, ls_depth + z2,
                  ls_height + ls_indent_height + z2])
    cutout = translate([-z, -z, -z])(cutout)
    indent = cube([ls_indent_width, ls_depth, ls_indent_height])
    inner_indent = translate([0, 0, ls_height])(indent)
    outer_indent = translate(
        [ls_width - ls_indent_width + z, 0, ls_height])(indent)
    return holder - cutout + inner_indent + outer_indent


def generate_model():
    roof = cube([width, depth, m])
    wall = cube([m, depth, height])
    holder = generate_light_strip_holder()
    holder = translate([m, depth / 2 - ls_depth / 2, m])(holder)
    return roof + wall + holder


model = generate_model()

scad_render_to_file(model, "light-strip-attachment.scad",
                    file_header=f"$fn = {fn};")
