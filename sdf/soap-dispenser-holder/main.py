from sdf import *
import math

cm = 10  # Centimeters
r = 5*cm  # Radius of holder
h = 1*cm  # Height of holder
bm = 0.3*cm  # Bottom margin

rt = 4*cm  # Radius of holder tip
dt = 8*cm  # Distance to holder tip (from holder)
rd = 4*cm  # Radius of soap dispenser
sm = r-rd  # Side margin

# Holder
f = rounded_cone(r, rt, dt)
f = f.orient(-X).slice().extrude(h)

# Indent for soap dispenser
x = rounded_cylinder(rd, h, h * 3).translate((0, 0, bm+h))
f -= x

# Soap catcher
l = 8*h
a = (rt-sm)*2.2
b = (rt-sm)*0.2
x = rounded_cone(a, b, l)
x = x.rotate(pi/2 - math.atan2(b - a, l) + pi/14, Y)
x = x.translate((dt*1, 0, a - h/2 + bm))
f -= x.k(0.2*cm)

f.save('soap-dispenser-holder.stl', step=3)
