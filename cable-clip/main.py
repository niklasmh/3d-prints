from solid import *
from solid.utils import *
import math

cm = 10
z = 0.01

wire_radius = 0.25*cm
height = 1*cm
wall_thickness = 0.1*cm
gap_between_wires = 0.2*cm
input_gap_left = 0.32*cm
input_gap_right = 0.28*cm

second_wire_distance = gap_between_wires + 2*wire_radius

input_left = input_gap_left * math.cos(
    math.pi/2 - math.asin(input_gap_left / 2 / wire_radius)
) / 2 + wall_thickness
input_right = input_gap_right * math.cos(
    math.pi/2 - math.asin(input_gap_right / 2 / wire_radius)
) / 2 + wall_thickness

wire_hole = cylinder(wire_radius, height + 2*z)
wire_input_left = cube(
    [input_left, 2*(wire_radius+wall_thickness), height + 2*z])
wire_input_left = cube(
    [input_left, 2*(wire_radius+wall_thickness), height + 2*z])
wire_input_right = cube(
    [input_right, 2*(wire_radius+wall_thickness), height + 2*z])
wire_holes = (
    translate([0, 0, -z])(wire_hole) +
    translate([second_wire_distance, 0, -z])(wire_hole) +
    translate([-wire_radius-wall_thickness, -
               wire_radius-wall_thickness, -z])(wire_input_left) +
    translate([second_wire_distance+wire_radius+wall_thickness-input_right, -
               wire_radius-wall_thickness, -z])(wire_input_right)
)

wire_shell = cylinder(wire_radius + wall_thickness, height)
wire_shells = (
    translate([0, 0, 0])(wire_shell) +
    translate([second_wire_distance, 0, 0])(wire_shell)
)

clip = hull()(wire_shells) - wire_holes

fn = 32
scad_render_to_file(clip, "cable-clip.scad",
                    file_header='$fn = %d;' % fn)
