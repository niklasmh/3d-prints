#!/usr/bin/env python3

import os
import subprocess
import argparse
import shutil
import pathlib
import random

parser = argparse.ArgumentParser(add_help=False,
                                 description='Generate mesh models from SDF using marching cubes.')

parser.add_argument("file", help="Python filename (with extension)")
parser.add_argument("-w", "--watch", action="store_true",
                    help="Generate new mesh when file is changed")
parser.add_argument("-p", "--preview", action="store_true",
                    help="Preview mesh in browser")
parser.add_argument('--help', action='help', default=argparse.SUPPRESS,
                    help='Show this help message and exit.')
args = parser.parse_args()

FILENAME = args.file[:-3] if args.file[-3:] == ".py" else args.file
MESH_FILE = FILENAME + ".stl"
WATCH = args.watch
PREVIEW = args.preview


if PREVIEW and WATCH:
    command = "npm run dev"
    folder = "preview"
    output = subprocess.Popen(command, cwd=folder, env=os.environ, shell=True)


if WATCH:
    command = f"nodemon run.py {FILENAME}.py"
    subprocess.run(command, env=os.environ, shell=True)
    exit(0)


def pj(path1, path2):
    return os.path.join(path1, path2)


def mkdir(dir):
    pathlib.Path(dir).mkdir(parents=True, exist_ok=True)


# Run the mesh generator

command = "docker-compose run sdf"
env = os.environ.copy()
env["FILE"] = FILENAME + ".py"
folder = "generate"
subprocess.run(command, cwd=folder, env=env, shell=True)


# Output files to the previewer

PREVIEW_FOLDER = "preview/src/assets"
PREVIEW_INFO_FILE = pj(PREVIEW_FOLDER, "info.txt")
PREVIEW_MESH_FILE = pj(PREVIEW_FOLDER, "mesh.stl")

mkdir(PREVIEW_FOLDER)
shutil.copyfile(MESH_FILE, PREVIEW_MESH_FILE)

with open(PREVIEW_INFO_FILE, "w") as f:
    id = random.randint(1000, 9999)
    f.write(f"stl {id} {FILENAME}")

if PREVIEW and not WATCH:
    command = "npm run dev"
    folder = "preview"
    output = subprocess.Popen(command, cwd=folder, env=os.environ, shell=True)
    output.communicate()