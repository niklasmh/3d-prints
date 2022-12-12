from sdf import *

cm = 10  # Centimeters
m = 0.4*cm  # Margin
m2 = m*2
r = 2*cm  # Radius
r2 = r*2

b = box(r2)
hole = box((r2-m2, r2-m2, r2))
b -= hole.orient(X) | hole.orient(Y) | hole

s = sphere(r)

f = s | b
f.save('ball-in-cube.stl', step=1.5)
