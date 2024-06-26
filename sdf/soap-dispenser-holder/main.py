from sdf import *
import math

cm = 10  # Centimeters
r = 4*cm  # Radius of holder
h = 1*cm  # Height of holder
bm = 0.3*cm  # Bottom margin

rt = 3*cm  # Radius of holder tip
dt = 8*cm  # Distance to holder tip (from holder)
rd = 3.7*cm  # Radius of soap dispenser
rdb = 3*cm  # Radius of soap dispenser bottom
sdc = 0.7*cm  # Soap dispenser bottom cut
sm = r-rd  # Side margin

# Holder
f = rounded_cone(r, rt, dt)
f = f.orient(-X).slice().extrude(h)

# Indent for soap dispenser
x = rounded_cylinder(rd, rdb, h*10).translate((0, 0, h*5))
x &= plane().translate((0, 0, sdc))
f -= x.translate((0, 0, bm-h/2-sdc))

# Soap catcher
l = 8*h
a = (rt-sm)*2.2
b = (rt-sm)*0.2
x = rounded_cone(a, b, l)
x = x.rotate(pi/2 - math.atan2(b - a, l) + pi/20, Y)
x = x.translate((dt*0.8, 0, a - h/2 + bm))
f -= x.k(0.2*cm)

f = f.rotate(pi/4, Z)

f.save('soap-dispenser-holder.stl', step=0.2)
