from solid import *
from solid.utils import *

cm = 10

width = 2*cm
head_stand_width = 6.5*cm
height = 3*cm
gap = 0.1*cm
m = 1*cm

hook = linear_extrude(height=width, slices=1)(
    polygon([
        [0, 0],
        [0, -height-m],
        [m+gap+m, -height-m],
        [m+gap+m, 0],
        [m+gap+m+head_stand_width, 0],
        [m+gap+m+head_stand_width, -height],
        [m+gap+m+head_stand_width+m, -height],
        [m+gap+m+head_stand_width+m, m],
        [m+gap+m, m],
        [m+gap, m],
        [m+gap, -height],
        [m, -height],
        [m, 0],
    ])
)

fn = 9
scad_render_to_file(hook, "magnetic-night-stand.scad",
                    file_header='$fn = %d;' % fn)
