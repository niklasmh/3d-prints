import sys
import os
from openpyscad import *

filename = ".".join(__file__.split(".")[:-1])

ball = Sphere(r=10, _fn=100)
hull = Sphere(r=5, _fn=100).translate([  0,   0,  10]) \
      + Sphere(r=5, _fn=50).translate([  0,   0, -10]) \
      + Sphere(r=5, _fn=50).translate([  0,  10,   0]) \
      + Sphere(r=5, _fn=50).translate([  0, -10,   0]) \
      + Sphere(r=5, _fn=50).translate([ 10,   0,   0]) \
      + Sphere(r=5, _fn=50).translate([-10,   0,   0])

(ball - hull).write(filename + ".scad", with_print=True)
