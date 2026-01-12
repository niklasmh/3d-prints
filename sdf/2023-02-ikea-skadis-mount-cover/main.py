from sdf import *

cm = 10  # Centimeters
m = 0.2*cm  # Margin
WIDTH = 2*cm
LENGTH = 5.1*cm
HEIGHT = 4.7*cm
BOTTOM_PIECE_RADIUS = 3.1*cm / 2
BOTTOM_PIECE_OFFSET = 1.88*cm
BOTTOM_PIECE_HEIGHT = 0.2*cm


def cover():
    inside = box((WIDTH, LENGTH, HEIGHT*2))
    cover = rounded_box((WIDTH + m*2, LENGTH + m*2, HEIGHT*2 + m*2), 2.5)
    cover &= plane(UP)
    bottom_piece = capped_cylinder(0, Z, BOTTOM_PIECE_RADIUS)
    bottom_piece = bottom_piece.scale((1, 1, BOTTOM_PIECE_HEIGHT))
    bottom_piece = bottom_piece.translate(
        (0, BOTTOM_PIECE_OFFSET - LENGTH / 2, 0))
    cover -= bottom_piece
    return cover - inside - inside.translate((0, 0, -HEIGHT / 2))


cover().save('ikea-skadis-mount-cover.stl', step=0.2)
