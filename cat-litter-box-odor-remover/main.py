import numpy as np
from solid import *
from solid.utils import *

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
save = lambda m, n: scad_render_to_file(m, n, file_header='$fn = 64;')


# Parameters
w_fan = 140 + m # Width of fan
h_fan = 140 + m # Height of fan
d_fan = 24 + m # Depth of fan
r_fan = 134 / 2 # Radius
ox_fan_hole = 7 + m # Offset x of fan screw hole
oy_fan_hole = 7 + m # Offset y of fan screw hole
r_fan_hole = 2.5 # Radius of fan screw hole
re_fan_hole = 13 # Extra radius of fan screw hole
d_fan_hole = 5 # Depth of fan screw hole

x_ihose = 0.15 * w_fan # Offset x of hose input connector
y_ihose = 0.50 * h_fan # Offset y of hose input connector
x_ohose = 0.25 * w_fan # Offset x of hose output connector
y_ohose = 0.40 * w_fan / 2 # Offset y of hose output connector
r_hose = 13 # Radius of hose connector
m_hose = 3 # Margin of hose connector
d_hose = 30 # Depth of hose connector

h_adapter = 2 # Height of adapter
w_adapter = 120 # Width of adapter attachment
d_adapter = 3 # Depth of adapter attachment


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


def create_input_adapter():
  m = 5 # Margin

  # The input hole for the air flow
  adapter_hole = cube([w_adapter - m * 2, d_adapter + m * 3, h_adapter + z2])
  adapter_hole = txy(adapter_hole, m, -m - z)
  adapter_hole = tz(adapter_hole, -z)
  left_side_hole = cube([m + z, d_adapter, h_adapter + z2])
  left_side_hole = tz(left_side_hole, -z)
  right_side_hole = left_side_hole
  left_side_hole = tx(left_side_hole, -m - z)
  right_side_hole = tx(right_side_hole, w_adapter)
  side_holes = left_side_hole + right_side_hole

  # The shape that meets the litter box
  adapter_interface = cube([w_adapter + m * 2, d_adapter + m, h_adapter])
  adapter_interface = tx(adapter_interface, -m)

  # The shape outside of the litter box
  adapter_frame = cube([w_adapter + m * 2, m, h_adapter + m * 2])
  adapter_frame = txy(adapter_frame, -m, -m)
  adapter_frame = tz(adapter_frame, -m)

  adapter = adapter_interface + adapter_frame

  return adapter - adapter_hole - side_holes


fan_box_input = create_fan_box_input()
fan_box_output = create_fan_box_output()
input_adapter = create_input_adapter()


import os
folder = os.path.basename(os.path.dirname(__file__))
save(rx(fan_box_input, 90) + ty(tz(rx(fan_box_output, -90), h_fan), d_fan), folder + ".assembly.scad")
save(fan_box_input, folder + ".fan-box-input.scad")
save(fan_box_output, folder + ".fan-box-output.scad")
save(input_adapter, folder + ".input-adapter.scad")
