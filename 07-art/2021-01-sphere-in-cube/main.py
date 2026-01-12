from openpyscad import *

r = 10
margin = 2
sphere = Sphere(r)
avoid_z_fighting = 0.001
cube = Cube([r*2, r*2, r*2]).translate([-r, -r, -r])
inside_cube = Cube([r*2 - margin*2, r*2 - margin*2, r *
                    2 - margin*2]).translate([-r, -r, -r])
hole = (
    inside_cube.translate([margin*3, margin, margin])
    + inside_cube.translate([margin*-3, margin, margin])
    + inside_cube.translate([margin, margin*3, margin])
    + inside_cube.translate([margin, margin*-3, margin])
    + inside_cube.translate([margin, margin, margin*3])
    + inside_cube.translate([margin, margin, margin*-3])
)

(
    cube
    - hole
    + sphere
).write("sphere-in-cube.scad")
