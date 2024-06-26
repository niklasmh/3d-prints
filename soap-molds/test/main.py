from numpy import *
from numpy.linalg import *
from solid import *
from solid.utils import *


def create_shape():
    shape = import_stl('duck.stl')
    bx = [-50, 50]
    by = [-62, 62]
    bz = [-30, 78]
    ox = 0
    oy = -10
    return shape, (bx, by, bz), (ox, oy)


def create_mold(shape, aabb, origin, n=4, print_to_files=False):
    bx, by, bz = aabb
    dx = bx[1] - bx[0]
    dy = by[1] - by[0]
    dz = bz[1] - bz[0]
    ox = bx[0] + dx / 2
    oy = by[0] + dy / 2
    rx = dx / 2
    ry = dy / 2

    model = cube(0)
    points = [[rx, 0]]
    molds = []
    pa = 0
    for a in linspace(0, 2*pi, n + 1, endpoint=True)[1:]:
        px = rx * cos(pa)
        py = ry * sin(pa)
        qx = rx * cos(a)
        qy = ry * sin(a)
        points.append([qx, qy])

        mold_part = polygon(points=[
            origin,
            [ox + px, oy + py],
            [ox + qx, oy + qy],
        ])
        mold_part = linear_extrude(dz)(mold_part)
        mold_part = translate((0, 0, bz[0]))(mold_part)
        mold_part -= shape
        mold_part = color([1, 1, 0], 0.5)(mold_part)
        model += mold_part

        slope = atan2(qy - py, qx - px)
        o = array(origin)
        p = array((ox + px, oy + py))
        q = array((ox + qx, oy + qy))
        d = abs(cross(p - q, o - q)) / norm(p - q)
        mold_part = translate((-origin[0], -origin[1], 0))(mold_part)
        mold_part = rotate((0, 0, -slope / pi * 180))(mold_part)
        mold_part = translate((0, d, -dz - bz[0]))(mold_part)
        mold_part = rotate((90, 0, 0))(mold_part)

        molds.append(mold_part)
        pa = a

    if print_to_files:
        import pathlib
        pathlib.Path('molds').mkdir(exist_ok=True)
        for i, mold in enumerate(molds):
            scad_render_to_file(mold, f"mold-{i + 1}.scad")

    def sc(points, scale):
        return [[p[0]*scale, p[1]*scale] for p in points]
    scaffold = polygon(points=sc(points, 1.1) + sc(points[::-1], 1))
    scaffold_bottom = polygon(points=sc(points, 1.1))
    scaffold = linear_extrude(15)(scaffold)
    scaffold_bottom = linear_extrude(3)(scaffold_bottom)
    scaffold = translate((0, 0, bz[0] - 3))(scaffold)
    scaffold_bottom = translate((0, 0, bz[0] - 3))(scaffold_bottom)
    scaffold += scaffold_bottom

    if print_to_files:
        import pathlib
        pathlib.Path('molds').mkdir(exist_ok=True)
        scad_render_to_file(scaffold, "mold-scaffold.scad")
    model += scaffold

    return model, molds


shape, aabb, origin = create_shape()
model, _ = create_mold(shape, aabb, origin, n=8, print_to_files=True)

scad_render_to_file(shape + model, 'mold.scad')
