from sdf import *

cm = 10  # Centimeters
m = 0.4*cm  # Margin
SINK_TIP_WIDTH = 4.45*cm
SINK_TIP_HEIGHT = 2.1*cm
SINK_TIP_LENGTH = 12.2*cm
SINK_TIP = 0.8*cm
SINK_TIP_RADIUS = 1*cm


def sink():
    cut_plane = plane(-UP).translate((0, 0, 0.2*cm))
    return box((SINK_TIP_WIDTH, SINK_TIP_LENGTH + SINK_TIP, SINK_TIP_HEIGHT)) | cut_plane


def smooth_surface():
    r = SINK_TIP_WIDTH / 2 * 1.1
    scale = (1, 1, 0.5)
    t = (0, -SINK_TIP, r * scale[2])
    return rounded_cylinder(r, SINK_TIP_RADIUS, SINK_TIP_LENGTH + SINK_TIP).orient(Y).translate(t).scale(scale)


(smooth_surface() - sink()).save('sink-fix.stl', step=0.2)
