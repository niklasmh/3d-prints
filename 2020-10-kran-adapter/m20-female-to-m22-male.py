from openpyscad import *
from math import *


def generate_helix(radius, height, steps, rotation_steps, height_offset = 0, rotation_offset = 0):
  helix = []
  angle = 0
  step = 0
  d_step = height / steps

  while step < height:
    d_rotation = 2 * pi / rotation_steps
    rotation = rotation_offset

    while rotation < 2 * pi - d_rotation + rotation_offset:
      helix.append([-sin(rotation)*radius, cos(rotation)*radius, step+d_step*rotation/(2*pi)+height_offset])
      rotation += d_rotation

    step += d_step
  helix.append([-sin(rotation)*radius, cos(rotation)*radius, step+d_step*(rotation/(2*pi) - 1)+height_offset])

  return helix


def create_screw(radius, height, steps, rotation_steps, depth):
  d_step = height / steps
  outer_helix = generate_helix(radius, height + d_step*2, steps + 2, rotation_steps, height_offset=-height/steps/2)
  inner_helix = generate_helix(radius - depth, height + d_step*2, steps + 2, rotation_steps, height_offset=-height/steps)
  points = []
  faces = []

  for i in range(0, len(outer_helix)):
    op = outer_helix[i]
    ip = inner_helix[i]
    points.append(ip)
    points.append(op)

  for i in range(1, len(outer_helix)):
    faces.append([i*2-2, i*2, i*2-1])
    faces.append([i*2, i*2+1, i*2-1])
    faces.append([(i+rotation_steps)*2-2, i*2-1, (i+rotation_steps)*2])
    faces.append([(i+rotation_steps)*2, i*2-1, i*2+1])

  faces.append([0, 1, rotation_steps*2])
  for i in range(1, rotation_steps):
    faces.append([0, i*2+2, i*2])

  last_index = len(points) - 1
  faces.append([last_index, last_index - 1, last_index - rotation_steps*2])
  for i in range(2, rotation_steps + 1):
    faces.append([last_index, last_index - i*2, last_index - i*2+2])

  """
  import matplotlib.pyplot as plt
  import numpy as np

  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')

  xs = [p[0] for p in outer_helix]
  ys = [p[1] for p in outer_helix]
  zs = [p[2] for p in outer_helix]
  ax.scatter(xs, ys, zs, marker='o')

  xs = [p[0] for p in inner_helix]
  ys = [p[1] for p in inner_helix]
  zs = [p[2] for p in inner_helix]
  ax.scatter(xs, ys, zs, marker='o')

  ax.set_xlabel('X Label')
  ax.set_ylabel('Y Label')
  ax.set_zlabel('Z Label')

  plt.show()
  #"""

  cube = Cube([radius*2, radius*2, height]).translate([-radius, -radius])
  top_cube = cube.translate([0, 0, height])
  bottom_cube = cube.translate([0, 0, -height])

  return Polyhedron(points=points, faces=faces) - (top_cube + bottom_cube)


m20 = create_screw(20.5/2, 5, 5, 42, 1).translate([0, 0, 4])
m22 = create_screw(22/2, 4, 4, 42, 1)
outer_cylinder = Cylinder(4, 11).translate([0,0,4])
inner_cylinder = Cylinder(8, 8)

filename = ".".join(__file__.split(".")[:-1])

# Composing the resulting shape using the existing shapes
(m22 + outer_cylinder - m20 - inner_cylinder).write(filename + ".scad")
