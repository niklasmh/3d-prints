from solid import *
from solid.utils import *
from math import *

# Constants
cm = 10
z = 0.01  # Fix z-fighting
z2 = 2*z
fn = 32  # Circle details
text_content = "Nei til reklame"
font_size = 4

# Physical measurements
d = 0.15*cm  # Depth of plate
w = 4.0*cm  # Width of plate
h = 1.0*cm  # Height of plate
text_d = 0.1*cm  # Depth of text
rounded_corner = 0.2*cm


def generate_plate():
    plate = cube([w - rounded_corner * 2, h - rounded_corner * 2, d])
    plate = translate([rounded_corner, rounded_corner, 0])(plate)
    plate = minkowski()(plate, cylinder(rounded_corner, 0.1))
    plate = color([1, 0, 0])(plate)

    return plate


def generate_text():
    text_element = text(text_content, font_size,
                        halign="center", valign="center", font="Arial:style=Bold")
    text_element = color([1, 1, 1])(text_element)
    text_element = linear_extrude(text_d)(text_element)
    text_element = translate([w/2, h/2, d])(text_element)
    return text_element


model = generate_plate() + generate_text()

scad_render_to_file(model, "no-to-ads-on-mailbox.scad",
                    file_header=f"$fn = {fn};")
