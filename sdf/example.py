from sdf import *

cm = 10

f = sphere(1.0*cm) & box(2*cm)

c = cylinder(0.5*cm)
f -= c.orient(X) | c.orient(Y) | c.orient(Z)

f.save('example.stl')
