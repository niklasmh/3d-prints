import math
from openpyscad import *


def cm(value):
    # Function for scaling from cm to mm (or what is desired)
    return value / 0.1


# Constants
device_depth = cm(1)
device_width = cm(6.8)
device_height = cm(13.5)
margin = cm(0.025)  # Space between parts
avoid_z_fighting = 0.01
pipe_width = cm(0.5)  # device_depth
charger_radius = cm(4.6)
charger_depth = cm(1)
charger_center = pipe_width + device_height / 2

width = (charger_radius + pipe_width) * 2
charger_center = charger_center
grow = charger_radius / 2

# Shapes
charger = (
    Cylinder(charger_depth + avoid_z_fighting, charger_radius)
    .rotate([-90, 0, 0])
    .translate([pipe_width + charger_radius, device_depth - avoid_z_fighting, charger_center])
)

device = Cube([device_width, device_depth + avoid_z_fighting, device_height])
device_portrait = (
    device
    .translate([width / 2 - device_width / 2, -avoid_z_fighting, pipe_width])
)
device_landscape = (
    device
    .rotate([0, 90, 0])
    .translate([width / 2 - device_height / 2, -avoid_z_fighting, charger_center + device_width / 2])
)

dx = width / 2 - device_width / 2 - pipe_width
dy = charger_center - device_width / 2
skew_angle = math.atan2(dx, dy) * 180 / math.pi
device_skew_left = (
    device
    .rotate([0, -skew_angle, 0])
    .translate([width / 2 - device_width / 2, -avoid_z_fighting, pipe_width])
)
device_skew_right = (
    device
    .rotate([0, -skew_angle, 0])
    .scale([-1, 1, 1])
    .translate([width / 2 + device_width / 2, -avoid_z_fighting, pipe_width])
)

front = (
    Cube([width, pipe_width, charger_center])
    - (device_portrait + device_landscape)
    - (device_skew_left + device_skew_right)
)

charger_container = (
    Cube([width, pipe_width + charger_depth + device_depth,
          device_width / 2 + pipe_width + grow])
    .translate([0, 0, charger_center - pipe_width - device_width / 2])
    - charger
    - (device_portrait + device_landscape)
    - (device_skew_left + device_skew_right)
)

bottom_depth = pipe_width * 2 * 6
bottom = (
    Cube([width, bottom_depth, pipe_width * 1.5])
    .translate([0, -pipe_width / 2, -pipe_width * 0.8])
)
for i in range(5):
    bottom -= (
        Cube([width + avoid_z_fighting*2, pipe_width + margin*2, pipe_width*2])
        # .scale([1, -1, 1])
        .translate([0, -pipe_width / 2, -pipe_width / 2])
        .rotate([-30 + i*(30/4), 0, 0])
        .translate([-avoid_z_fighting, pipe_width + pipe_width*2*i, pipe_width / 2 - margin])
    )


# Build the main part
main_part = (
    front
    + charger_container
)

# Build the bottom
bottom_part = (
    bottom
)

# Render each model to separate files
main_part.write("main-part.scad")
bottom_part.write("bottom-part.scad")

# Render all the models to the same file
(
    main_part
    + bottom_part.translate([0, 0, -pipe_width])
).write("all-parts.scad")
