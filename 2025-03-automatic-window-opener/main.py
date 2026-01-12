import numpy as np
from solid import *
from solid.utils import *

z = 0.1
z2 = 0.2

t = translate
r = rotate
sc = scale
cos = np.cos
sin = np.sin
pi = np.pi
save = lambda m, n: scad_render_to_file(m, n, file_header='$fn = 64;')

# Parameters
ro_gear = 45 / 2 # Outer radius of gear
d_teeth = 4 # Depth of teeth
ri_gear = ro_gear - d_teeth # Inner radius of gear
d_gear = 13 # Depth of gear
n_gear = 12 # Teeth count
r_gear_mount = 6.4 / 2 # Radius of gear mount hole
d_gear_mount = 12 # Depth of gear mount
c_gear_mount = 1.6 # Gear mount cut depth from center
gear_offset = 40 # Offset of gear from rail tangent (affects twist of gear teeth)

ro_rail = 300 # Outer radius from hinge to rail
d_rail = d_gear # Depth of rail
ri_rail = ro_rail - d_rail # Inner radius from hinge to rail
a_rail = 38 # Angle of rail
h_rail = 10 # Height of rail
n_rail = n_gear * ro_rail / ro_gear


def trail_pattern(p):
  return cos(p * pi) ** 4


def create_rail():
  points = []
  faces = []

  for i, a in enumerate(np.linspace(0, a_rail / 180 * pi, 512)):
    ri = ri_rail
    ro = ro_rail
    x = cos(a)
    y = sin(a)
    progress = a / (pi * 2) * n_rail
    z = h_rail + (1 - trail_pattern(progress)) * d_teeth
    points.append([x * ri, y * ri, 0])
    points.append([x * ro, y * ro, 0])
    points.append([x * ri, y * ri, z])
    points.append([x * ro, y * ro, z])
    p1 = 4 * i
    p2 = 4 * (i + 1)
    faces.append([p1 + 0, p1 + 1, p2 + 1, p2 + 0])
    faces.append([p1 + 1, p1 + 3, p2 + 3, p2 + 1])
    faces.append([p2 + 0, p2 + 2, p1 + 2, p1 + 0])
    faces.append([p2 + 2, p2 + 3, p1 + 3, p1 + 2])

  faces.append([2, 3, 1, 0])
  lp = len(points)
  faces.append([lp - 4, lp - 3, lp - 1, lp - 2])

  min_x = min(p[0] for p in points)
  max_x = max(p[0] for p in points)
  min_y = min(p[1] for p in points)
  max_y = max(p[1] for p in points)
  center = [-(min_x + max_x) / 2, -(min_y + max_y) / 2, 0]

  return t(center)(polyhedron(points=points, faces=faces))


def create_gear():
  points = []

  for i in range(n_gear):
    da = 2 * pi / n_gear # Delta angle
    for progress in np.linspace(0, 1, 32):
      r = ri_gear + trail_pattern(progress) * d_teeth
      a = (i + progress) * da
      x = r * cos(a)
      y = r * sin(a)
      points.append([x, y])

  cut = cube([2 * r_gear_mount, 2 * r_gear_mount, d_gear_mount])
  cut = t([c_gear_mount, -r_gear_mount, 0])(cut)
  hole = cylinder(r=r_gear_mount, h=d_gear_mount) - cut
  hole = t([0, 0, -z])(hole)

  offset_twist = np.atan2(-gear_offset, ro_rail) * 180 / pi

  return linear_extrude(height=d_gear, slices=1, twist=offset_twist)(polygon(points)) - hole


rail = create_rail()
gear = create_gear()

save(color("red")(t([10, -3.5, ro_gear + h_rail + 1])(r([-6, 90, 0])(gear))) + rail, "automatic-window-opener.assembly.scad")
save(gear, "automatic-window-opener.gear.scad")
save(rail, "automatic-window-opener.rail.scad")
