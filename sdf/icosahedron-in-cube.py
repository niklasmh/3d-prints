from sdf import *

cm = 10  # Centimeters
m = 0.5*cm  # Margin
m2 = m*2
r = 2*cm  # Radius
r2 = r*2

b = box(r2)
hole = box((r2-m2, r2-m2, r2))
b -= hole.orient(X) | hole.orient(Y) | hole

s = icosahedron(r+m/2)

f = s | b
f.save('icosahedron-in-cube.stl', step=1.5)
