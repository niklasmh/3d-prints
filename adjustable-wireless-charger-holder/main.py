from openpyscad import *


def cm(value):
    # Function for scaling from cm to mm (or what is desired)
    return value / 0.1


# Values
device_depth = cm(1)
device_width = cm(6.8)
pipe_width = device_depth
wireless_charger_radius = cm(4.5)
wireless_charger_depth = cm(1)
min_height_above_ground = wireless_charger_radius + cm(4.5)

width = (wireless_charger_radius + pipe_width) * 2
height = min_height_above_ground
grow = wireless_charger_radius / 2

# Shapes
bottom_pipe = Cube([width, pipe_width, pipe_width])

left_pipe = Cube([pipe_width, pipe_width, height - device_width / 2])
left_pipe_flick = Cube(
    [pipe_width, wireless_charger_depth + pipe_width, pipe_width])
left_pipe_flick = left_pipe_flick.translate(
    [0, 0, height - pipe_width - device_width / 2])
left_pipe_wall = Cube(
    [pipe_width, pipe_width, device_width / 2 + grow])
left_pipe_wall = left_pipe_wall.translate(
    [0, pipe_width, height - device_width / 2])

right_pipe = Cube([pipe_width, pipe_width, height - device_width / 2])
right_pipe = right_pipe.translate([width - pipe_width, 0, 0])
right_pipe_flick = Cube(
    [pipe_width, wireless_charger_depth + pipe_width, pipe_width])
right_pipe_flick = right_pipe_flick.translate(
    [width - pipe_width, 0, height - pipe_width - device_width / 2])
right_pipe_wall = Cube(
    [pipe_width, pipe_width, device_width / 2 + grow])
right_pipe_wall = right_pipe_wall.translate(
    [width - pipe_width, pipe_width, height - device_width / 2])

wireless_charger = Cylinder(wireless_charger_depth, wireless_charger_radius)
wireless_charger = wireless_charger.rotate([-90, 0, 0])
wireless_charger = wireless_charger.translate(
    [pipe_width + wireless_charger_radius, pipe_width, height])

wireless_charger_back = Cube(
    [width, pipe_width, device_width / 2 + pipe_width + grow])
wireless_charger_back = wireless_charger_back.translate(
    [0, wireless_charger_depth + pipe_width, height - pipe_width - device_width / 2])

hole_width = pipe_width / 2
hole_margin = (pipe_width - hole_width) / 2
hole = Cylinder(pipe_width + hole_width / 4, hole_width / 2).rotate([0, 90, 0]).translate(
    [-hole_width/8, pipe_width + hole_margin * 2, height - device_width / 2 - pipe_width + hole_margin * 2])
adjust_holes_left = (
    hole
    + hole.translate([0, 0, pipe_width])
    + hole.translate([0, 0, pipe_width*2])
    + hole.translate([0, 0, pipe_width*3])
    + hole.translate([0, 0, pipe_width*4])
)
adjust_holes_right = adjust_holes_left.translate([width - pipe_width, 0, 0])
adjust_holes = adjust_holes_left + adjust_holes_right

bottom_hole_depth = cm(0.5)
bottom_hole_left = Cylinder(
    bottom_hole_depth*2, hole_width / 2).rotate([0, 90, 0]).translate([-bottom_hole_depth, pipe_width / 2, pipe_width / 2])
bottom_hole_right = bottom_hole_left.translate(
    [width, 0, 0])
bottom_holes = bottom_hole_right + bottom_hole_left

# Build the main part
main_part = (
    bottom_pipe
    + left_pipe + left_pipe_flick + left_pipe_wall
    + right_pipe + right_pipe_flick + right_pipe_wall
    + wireless_charger_back
    + wireless_charger
    - adjust_holes
    - bottom_holes
)

# TODO: Build the bottom
# TODO: Build the support
# TODO: Build adjust support

# Render
main_part.write("main-part.scad", with_print=True)
