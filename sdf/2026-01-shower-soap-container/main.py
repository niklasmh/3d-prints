from sdf import *
import numpy as np

# Constants
HEIGHT = 188
WIDTH = 80
DEPTH = 110
THICKNESS = 4
ROUNDING_RADIUS = 5
HOLE_RADIUS = 12

# Calculations
outer_dims = np.array((WIDTH, DEPTH, HEIGHT))
inner_dims = outer_dims - 2 * THICKNESS

# Shapes
f = rounded_box(outer_dims, ROUNDING_RADIUS)
f -= rounded_box(inner_dims, ROUNDING_RADIUS - THICKNESS)

hole = cylinder(HOLE_RADIUS)
hole &= plane().translate((0, 0, 0))
f -= hole

# Export
f.save("shower-soap-container.stl", step=1)
