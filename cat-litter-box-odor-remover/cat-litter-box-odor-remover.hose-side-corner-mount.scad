// Generated by SolidPython 1.1.3 on 2025-06-22 17:41:13
$fn = 64;


difference() {
	union() {
		difference() {
			rotate_extrude(angle = 90) {
				translate(v = [15, 0, 0]) {
					rotate(a = [0, 0, 90]) {
						union() {
							circle(r = 15);
							translate(v = [-15, -15, 0]) {
								square(size = [15, 30]);
							}
						}
					}
				}
			}
			rotate_extrude(angle = 90) {
				translate(v = [15, 0, 0]) {
					rotate(a = [0, 0, 90]) {
						circle(r = 10);
					}
				}
			}
		}
		translate(v = [15, 0, 0]) {
			rotate(a = [90, 0, 0]) {
				linear_extrude(height = 30) {
					rotate(a = [0, 0, 90]) {
						union() {
							circle(r = 15);
							translate(v = [-15, -15, 0]) {
								square(size = [15, 30]);
							}
						}
					}
				}
			}
		}
		translate(v = [0, 15, 0]) {
			rotate(a = [0, -90, 0]) {
				rotate(a = [0, 0, 90]) {
					scale(v = [1, -1, 1]) {
						linear_extrude(height = 30) {
							rotate(a = [0, 0, 90]) {
								union() {
									circle(r = 15);
									translate(v = [-15, -15, 0]) {
										square(size = [15, 30]);
									}
								}
							}
						}
					}
				}
			}
		}
	}
	union() {
		rotate_extrude(angle = 90) {
			translate(v = [15, 0, 0]) {
				rotate(a = [0, 0, 90]) {
					circle(r = 10);
				}
			}
		}
		translate(v = [0, 0.1000000000, 0]) {
			translate(v = [15, 0, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 30.2000000000) {
						rotate(a = [0, 0, 90]) {
							circle(r = 10);
						}
					}
				}
			}
		}
		translate(v = [0.1000000000, 0, 0]) {
			translate(v = [0, 15, 0]) {
				rotate(a = [0, -90, 0]) {
					rotate(a = [0, 0, 90]) {
						scale(v = [1, -1, 1]) {
							linear_extrude(height = 30.2000000000) {
								rotate(a = [0, 0, 90]) {
									circle(r = 10);
								}
							}
						}
					}
				}
			}
		}
	}
}
/***********************************************
*********      SolidPython code:      **********
************************************************
 
import numpy as np
from solid import *
from solid.utils import *
import os

folder = os.path.basename(os.path.dirname(__file__))

z = 0.1
z2 = 0.2
m = 2

t = translate
tx = lambda e, x: t([x, 0, 0])(e)
ty = lambda e, x: t([0, x, 0])(e)
tz = lambda e, x: t([0, 0, x])(e)
txy = lambda e, x, y: t([x, y, 0])(e)

r = rotate
rx = lambda e, x: r([x, 0, 0])(e)
ry = lambda e, x: r([0, x, 0])(e)
rz = lambda e, x: r([0, 0, x])(e)

sc = lambda e, x: scale([x, x, x])(e)
sx = lambda e, x: scale([x, 1, 1])(e)
sy = lambda e, x: scale([1, x, 1])(e)
sxy = lambda e, x: scale([x, x, 1])(e)
sz = lambda e, x: scale([1, 1, x])(e)

cos = np.cos
sin = np.sin
pi = np.pi
save = lambda m, n: scad_render_to_file(m, n, file_header="$fn = 64;")


# Parameters
w_fan = 140 + m  # Width of fan
h_fan = 140 + m  # Height of fan
d_fan = 24 + m  # Depth of fan
r_fan = 134 / 2  # Radius
ox_fan_hole = 7 + m  # Offset x of fan screw hole
oy_fan_hole = 7 + m  # Offset y of fan screw hole
r_fan_hole = 2.5  # Radius of fan screw hole
re_fan_hole = 13  # Extra radius of fan screw hole
d_fan_hole = 5  # Depth of fan screw hole

x_ihose = 0.15 * w_fan  # Offset x of hose input connector
y_ihose = 0.50 * h_fan  # Offset y of hose input connector
x_ohose = 0.25 * w_fan  # Offset x of hose output connector
y_ohose = 0.40 * w_fan / 2  # Offset y of hose output connector
r_hose = 13  # Radius of hose connector
m_hose = 3  # Margin of hose connector
d_hose = 30  # Depth of hose connector

h_adapter = 2  # Height of adapter
w_adapter = 120  # Width of adapter attachment
d_adapter = 3  # Depth of adapter attachment
wd_adapter = 3  # Wall depth of adapter attachment

w_wall_mount = (r_hose - m_hose) * 2 + 5 * 4  # Width of wall mount
h_wall_mount = w_wall_mount  # Height of wall mount


def create_fan_box():
    d = w_fan / 2 - d_fan / 2
    fan_box = cube([w_fan, h_fan, d])
    fan = sphere(r=r_fan)
    fan = txy(fan, w_fan / 2, h_fan / 2)
    fan = tz(fan, -d_fan / 2)

    hole = cylinder(r=re_fan_hole, h=d + z2)
    hole = tz(hole, d_fan_hole)
    hole += cylinder(r=r_fan_hole, h=d + z2)
    ox, oy = ox_fan_hole, oy_fan_hole
    holes = txy(hole, ox, oy)
    holes += txy(hole, w_fan - ox, oy)
    holes += txy(hole, ox, h_fan - oy)
    holes += txy(hole, w_fan - ox, h_fan - oy)
    holes = tz(holes, -z)

    return fan_box - fan - holes


def create_fan_box_input():
    fan_box = create_fan_box()

    d = w_fan / 2 - d_fan / 2
    hose_input = cylinder(r=r_hose, h=d_hose)
    hose_input = txy(hose_input, x_ihose, y_ihose)
    hose_input = tz(hose_input, d)
    hose_input_hole = cylinder(r=r_hose - m_hose, h=d + d_hose + z2)
    hose_input_hole = txy(hose_input_hole, x_ihose, y_ihose)
    hose_input_hole = tz(hose_input_hole, -z)

    return fan_box + hose_input - hose_input_hole


def create_fan_box_output():
    fan_box = create_fan_box()

    d = w_fan / 2 - d_fan / 2
    hose_output = cylinder(r=r_hose, h=d_hose)
    hose_output = rx(hose_output, 90)
    hose_output = tx(hose_output, x_ohose)
    hose_output = tz(hose_output, y_ohose)
    hose_output_hole = cylinder(r=r_hose - m_hose, h=h_fan + d_hose + z2)
    hose_output_hole = rx(hose_output_hole, 90)
    hose_output_hole = txy(hose_output_hole, x_ohose, h_fan / 2)
    hose_output_hole = tz(hose_output_hole, y_ohose)

    return fan_box + hose_output - hose_output_hole


def create_litter_box_input_clamps():
    m = 6  # Margin

    clamp_hole = cube([m + z, m_hose + d_adapter + wd_adapter, h_adapter + z2])
    clamp_hole = txy(clamp_hole, -m - z, m)
    clamp_hole = tz(clamp_hole, -z)

    input_clamp = cube([m * 2.5, m_hose + d_adapter + wd_adapter + m * 2, h_adapter])
    input_clamp = tx(input_clamp, -m)
    input_clamp -= clamp_hole
    input_clamp = ty(input_clamp, -m_hose - wd_adapter)

    input_clamps = input_clamp + tz(tx(ry(input_clamp, 180), m * 4), h_adapter)

    return input_clamps


def create_litter_box_hose_input():
    m = 5  # Margin

    # The input hole for the air flow
    airflow_hole = cube(
        [w_adapter, d_adapter + wd_adapter + m * 3 + z2, h_adapter + z2]
    )
    airflow_hole = ty(airflow_hole, -m - z)
    airflow_hole = tz(airflow_hole, -z)

    # Shape of the rounded cat litter box
    r = 1000  # Radius of cat litter box
    indent = 2  # Indent of the cat litter box
    litter_box_shape = cylinder(r=r, h=r_hose * 2, segments=512 * r / 1000)
    litter_box_shape = txy(litter_box_shape, w_adapter / 2, r - indent)
    litter_box_shape = tz(litter_box_shape, -r_hose)

    # Hose input connector
    l_hose = w_adapter + m * 2 + d_hose
    hose_input = cylinder(r=r_hose, h=l_hose)
    hose_input += sphere(r=r_hose) - sphere(r=r_hose - m_hose)
    hose_input -= tz(cylinder(r=r_hose - m_hose, h=l_hose + z2), -z)
    hose_input = ry(hose_input, 90)
    hose_input = tz(hose_input, h_adapter / 2)
    hose_input = txy(hose_input, -m * 2, -r_hose)
    hose_input -= litter_box_shape
    hose_input -= airflow_hole
    hose_input = rx(hose_input, 90)
    hose_input = tz(hose_input, r_hose * 2)

    return hose_input


def get_pos_from_angle(angle, radius, offset_angle=0):
    """
    Get the x, y position from an angle and radius.
    :param angle: Angle in degrees.
    :param radius: Radius of the circle.
    :return: Tuple of (x, y) position.
    """
    angle_rad = np.deg2rad(angle + offset_angle)
    x = radius * cos(angle_rad)
    y = radius * sin(angle_rad)
    return x, y


def create_cake_slice(radius, angle_start, angle_end, height, offset_angle=0):
    """
    Create a cake slice shape from a circle.
    :param radius: Radius of the circle.
    :param angle_start: Start angle in degrees.
    :param angle_end: End angle in degrees.
    :param height: Height of the cake slice.
    :return: Cake slice shape.
    """
    x_start, y_start = get_pos_from_angle(angle_start, radius, offset_angle)
    x_end, y_end = get_pos_from_angle(angle_end, radius, offset_angle)

    points = [[0, 0], [x_start, y_start], [x_end, y_end], [0, 0]]

    return linear_extrude(height)(polygon(points))


def create_hose_wall_mount():
    m = 5  # Margin
    hd = h_wall_mount - m * 2  # Hose depth
    r = r_hose - m_hose  # Radius of the hose
    ro = r + m  # Outer radius of the hose

    # The wall mount for the hose
    wall_mount = cube([w_wall_mount, h_wall_mount, m])

    # The hose input connector
    w = ro * 2
    hose_input = cube([w, w / 2, hd])
    hose_input = txy(hose_input, -r - m, -r - m)
    hose_input += cylinder(r=w / 2, h=hd)
    hose_input -= tz(cylinder(r=r, h=hd + z2), -z)

    deg = 75  # Angle of the cake slice
    cake_slice = create_cake_slice(
        radius=100,
        angle_start=-deg,
        angle_end=deg,
        height=hd + z2,
        offset_angle=90,
    )
    cake_slice = tz(cake_slice, -z)
    hose_input -= cake_slice

    rounded_corner = cylinder(r=m / 2, h=hd, segments=24)
    x1, y1 = get_pos_from_angle(deg, ro / 2, offset_angle=90)
    rounded_corners = txy(rounded_corner, x1, y1) + txy(rounded_corner, -x1, y1)
    hose_input += rounded_corners

    hose_input = rx(hose_input, 90)
    hose_input = txy(hose_input, w_wall_mount / 2, h_wall_mount / 2 + hd / 2)
    hose_input = tz(hose_input, ro + m / 2)

    return wall_mount + hose_input


def create_hose_corner_mount(deg=0, fill_corner=False, round_edge=False):
    m = 5  # Margin
    r = r_hose - m_hose  # Radius of the hose
    ro = r + m  # Outer radius of the hose
    length = d_hose

    outer_shape = rz(
        circle(r=ro) + txy(square([ro, ro * 2]), -r - m, -r - m),
        deg,
    )

    inner_shape = rz(
        circle(r=r),
        deg,
    )

    bend_shell = rotate_extrude(angle=90)(tx(outer_shape, ro))
    bend_hole = rotate_extrude(angle=90)(tx(inner_shape, ro))
    bend = bend_shell - bend_hole

    outer_edge = linear_extrude(height=length)(outer_shape)
    inner_edge = linear_extrude(height=length + z2)(inner_shape)

    edge_a_shell = rx(outer_edge, 90)
    edge_a_shell = tx(edge_a_shell, ro)

    edge_a_hole = rx(inner_edge, 90)
    edge_a_hole = tx(edge_a_hole, ro)
    edge_a_hole = ty(edge_a_hole, z)

    edge_b_shell = outer_edge
    edge_b_shell = sy(edge_b_shell, -1)
    edge_b_shell = rz(edge_b_shell, 90)
    edge_b_shell = ry(edge_b_shell, -90)
    edge_b_shell = ty(edge_b_shell, ro)

    edge_b_hole = inner_edge
    edge_b_hole = sy(edge_b_hole, -1)
    edge_b_hole = rz(edge_b_hole, 90)
    edge_b_hole = ry(edge_b_hole, -90)
    edge_b_hole = ty(edge_b_hole, ro)
    edge_b_hole = tx(edge_b_hole, z)

    if fill_corner:
        corner_fill = cube([ro * 2, ro * 2, ro * 2])
        corner_fill -= tz(txy(cube([ro, ro, ro * 2 + z2]), -z, -z), -z)
        corner_fill = tz(corner_fill, -r - m)
        bend += corner_fill

        if not round_edge:
            round_corner = cube([m + z, m + z, ro * 2 + z2])
            round_corner -= cylinder(r=m, h=ro * 2 + z2)
            round_corner = tz(round_corner, -r - m - z)
            round_corner = txy(round_corner, ro * 2 - m, ro * 2 - m)
            bend -= round_corner

    if round_edge:
        round_edge_hole = cube([ro * 2 + length + z2, ro + z, ro * 2 + z2])
        round_edge_hole = tz(round_edge_hole, -r - m - z)
        round_edge_hole -= ry(cylinder(r=ro, h=ro * 2 + length + z2), 90)
        round_edge_hole = tx(round_edge_hole, -length - z)
        round_edge_hole = ty(round_edge_hole, ro)
        bend -= round_edge_hole
        edge_b_shell -= round_edge_hole

    shell = bend + edge_a_shell + edge_b_shell
    hole = bend_hole + edge_a_hole + edge_b_hole

    return shell - hole


def create_hose_inner_corner_mount():
    return create_hose_corner_mount(deg=180, fill_corner=True)


def create_hose_outer_corner_mount():
    return create_hose_corner_mount(deg=0)


def create_hose_outward_corner_mount():
    return create_hose_corner_mount(deg=180, fill_corner=True, round_edge=True)


def create_hose_side_corner_mount():
    return create_hose_corner_mount(deg=90)


# Create the fan box input and output, and the assembly
fan_box_input = create_fan_box_input()
fan_box_output = create_fan_box_output()
assembly = rx(fan_box_input, 90) + ty(tz(rx(fan_box_output, -90), h_fan), d_fan)
save(fan_box_input, folder + ".fan-box-input.scad")
save(fan_box_output, folder + ".fan-box-output.scad")
save(assembly, folder + ".assembly.scad")

# Create the litter box hose input, and clamps for it
# The clamps are separate from the hose input because:
# 1. Removes need of supports for the hose input
# 2. Printing them flat makes them more durable
save(create_litter_box_hose_input(), folder + ".litter-box.hose-input.scad")
save(create_litter_box_input_clamps(), folder + ".litter-box.input-clamps.scad")

# Create the wall mount for the hose
save(create_hose_wall_mount(), folder + ".hose-wall-mount.scad")
save(create_hose_inner_corner_mount(), folder + ".hose-inner-corner-mount.scad")
save(create_hose_outer_corner_mount(), folder + ".hose-outer-corner-mount.scad")
save(create_hose_outward_corner_mount(), folder + ".hose-outward-corner-mount.scad")
save(create_hose_side_corner_mount(), folder + ".hose-side-corner-mount.scad")
 
 
************************************************/
