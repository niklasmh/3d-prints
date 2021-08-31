from solid import *
from solid.utils import *
from numpy import linspace

cm = 10

count = 10
gap = 0.2*cm
middle_gap = 1*cm

width = 4*cm
length = 5*cm
height = 3*cm

wall_thickness = (width - middle_gap) / 2
bottom_thickness = 0.2*cm
z = 0.001

bottom = cube([width, length, bottom_thickness])
left_wall = translate([0, 0, bottom_thickness])(
    cube([wall_thickness, length, height]))
right_wall = translate([width-wall_thickness, 0, bottom_thickness]
                       )(cube([wall_thickness, length, height]))

gaps = []
for i in linspace(-gap, length, count + 2)[1:-1]:
    gaps.append(translate([-z, i, bottom_thickness+z])(
        cube([width+z*2, gap, height+z])))

scad_render_to_file(bottom + left_wall + right_wall -
                    gaps, "resistor-holder.scad")
