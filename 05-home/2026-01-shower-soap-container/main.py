from sdf import *
import math

# Constants
IS_SHAMPOO = False
HEIGHT = 192
WIDTH = 80 if IS_SHAMPOO else 150
DEPTH = 110
THICKNESS = 1
ROUNDING_RADIUS = 6
FONT = "/System/Library/Fonts/Supplemental/Futura.ttc"
TEXT = "SHAMPOO" if IS_SHAMPOO else "SHOWER GEL"
TEXT_WIDTH, _ = measure_text(FONT, TEXT, height=10)

# Shapes
f = rounded_box((WIDTH, DEPTH, HEIGHT), ROUNDING_RADIUS)
t = (
    text(FONT, TEXT, height=10)
    .extrude(1)
    .rotate(math.pi / 2, X)
    .translate((-WIDTH / 2 + TEXT_WIDTH / 2 + 9, -DEPTH / 2, HEIGHT / 2 * 0.8))
)
f -= t  # Create indentation before shelling
f = f.shell(THICKNESS)
f -= t  # Make a more precise indentation after shelling

# Export
f.save("shower-soap-container.stl", step=0.8)
