from solid import *
from solid.utils import *

cm = 10

thickness = 0.2*cm
z_fighting = 0.01
width = 1*cm
top_hook_height = 1.1*cm
top_hook_depth = 0.6*cm
bottom_hook_height = 0.8*cm
bottom_hook_depth = top_hook_depth + thickness

top_hook_hole = cube([top_hook_depth, thickness +
                      z_fighting*2, top_hook_height])
top_hook = translate([-thickness, z_fighting, -thickness])(
    cube([top_hook_depth + thickness*2, thickness, top_hook_height + thickness*2])
) - top_hook_hole

bottom_hook_bottom = cube(
    [bottom_hook_depth+thickness/2**.5, thickness, thickness])
bottom_hook = (
    bottom_hook_bottom
    + translate([-thickness, 0, 0])(
        cube([thickness, thickness, bottom_hook_height + thickness])
    )
    + translate([bottom_hook_depth, 0, 0.2*cm]
                )(rotate([0, 45, 0])(cube(thickness)))
    - translate([bottom_hook_depth+thickness/2**.5, 0, 0]
                )(cube(thickness*2))
)

hook = (
    translate([0, 0, bottom_hook_height + thickness*2])(top_hook)
    + bottom_hook
)

fn = 9
scad_render_to_file(hook, "hook-for-kitchen-pincer.scad",
                    file_header='$fn = %d;' % fn)
