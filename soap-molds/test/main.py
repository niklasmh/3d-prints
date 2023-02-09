from solid import *
from solid.utils import *


def create_shape():
    shape = import_stl('duck.stl')
    bx = [-42, 42]
    by = [-60, 60]
    bz = [-30, 78]
    dx = bx[1] - bx[0]
    dy = by[1] - by[0]
    dz = bz[1] - bz[0]
    return shape, (bx, by, bz, dx, dy, dz)


def create_mold(shape, aabb):
    bx, by, bz, dx, dy, dz = aabb
    gap = 5
    mold = cube((dx / 2, dy, dz))
    mold = color([1, 1, 0], 0.5)(mold)

    mold_left = translate((bx[0], by[0], bz[0]))(mold)
    mold_left -= shape
    mold_left = translate((0, 0, gap - bz[0]))(mold_left)
    mold_left = rotate((0, -90, 0))(mold_left)
    mold_left = translate((0, 0, -bx[0]))(mold_left)

    mold_right = translate((bx[1] - dx / 2, by[0], bz[0]))(mold)
    mold_right -= shape
    mold_right = translate((0, 0, gap - bz[0]))(mold_right)
    mold_right = rotate((0, 90, 0))(mold_right)
    mold_right = translate((0, 0, bx[1]))(mold_right)

    return mold_left + mold_right


# Remove shape from mold
shape, aabb = create_shape()
molds = create_mold(shape, aabb)

scad_render_to_file(molds, 'test-mold.scad')
