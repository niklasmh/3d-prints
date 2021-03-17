from solid import *
from solid.utils import *

cm = 10

couch_edge_width = 5.5*cm
height = 8*cm
thickness = 0.5*cm
width = 5*cm
couch_back_slope = 3 / 8  # dx / dy
hook_gap = 1*cm
hook_length = hook_gap + thickness
hook_start = -couch_back_slope * couch_edge_width

hook = linear_extrude(height=width, slices=1)(
    polygon([
        [0, -height],  # Starting from bottom and doing the inner path first
        [0, 0],
        [couch_edge_width, 0],
        [couch_edge_width + couch_back_slope*height, -height],
        [couch_edge_width + couch_back_slope*height + 0.2*cm, -height],
        [couch_edge_width + thickness, thickness],
        [-thickness, thickness],
        [-thickness, hook_start - thickness],  # Hook start
        [-thickness - hook_gap, hook_start - thickness],
        [-thickness - hook_gap, hook_start + thickness],
        [-thickness - hook_length, hook_start + thickness],
        [-thickness - hook_length, hook_start - thickness * 2],
        [-thickness, hook_start - thickness * 2],  # Hook end
        [-thickness, -height],
    ])
)

fn = 9
scad_render_to_file(hook, "hook-behind-couch.scad",
                    file_header='$fn = %d;' % fn)
