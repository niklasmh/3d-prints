#!/usr/bin/env python3

import argparse
import atexit
import os
import pathlib
import random
import signal
import shutil
import subprocess

parser = argparse.ArgumentParser(add_help=False,
                                 description='Generate mesh models from SDF using marching cubes.')

parser.add_argument(
    "file", help="Python filename (with .py-extension) OR folder (containing main.py file).")
parser.add_argument("-w", "--watch", action="store_true",
                    help="Generate new mesh when file is changed.")
parser.add_argument("-p", "--preview", action="store_true",
                    help="Preview mesh in browser.")
parser.add_argument('--help', action='help', default=argparse.SUPPRESS,
                    help='Show this help message and exit.')
args = parser.parse_args()


def pj(*paths):
    return os.path.join(*paths)


def ps(path):
    return os.path.normpath(path).split(os.sep)


def mkdir(dir):
    pathlib.Path(dir).mkdir(parents=True, exist_ok=True)


CURRENT_FILE = os.path.realpath(__file__)
CURRENT_FOLDER = os.path.dirname(CURRENT_FILE)

ENV = {}
ENV["PYTHON_COMMAND"] = "python"
ENV["USE_DOCKER"] = "false"
try:
    for line in open(".env").read().strip().split("\n"):
        key, value = line.split("=")
        ENV[key.strip()] = value.strip()
except:
    pass

USE_DOCKER = ENV["USE_DOCKER"] == "true"
PYTHON_COMMAND = ENV["PYTHON_COMMAND"]

IS_PYTHON_FILE = args.file[-3:] == ".py"
if IS_PYTHON_FILE:
    PATH = args.file[:-3]
    FILENAME = ps(PATH)[-1]
    PROJECT_NAME = FILENAME
    FOLDER = pj(*ps(PATH)[:-1])
    MESH_FILE = pj(CURRENT_FOLDER, FOLDER, FILENAME + ".stl")
else:
    PATH = args.file
    FILENAME = "main"
    PROJECT_NAME = ps(PATH)[-1]
    FOLDER = PATH
    MESH_FILE = pj(CURRENT_FOLDER, FOLDER, PROJECT_NAME + ".stl")
WATCH = args.watch
PREVIEW = args.preview


if PREVIEW and WATCH:
    command = "npm run dev"
    folder = "mesh-viewer"
    preview_process = subprocess.Popen(
        command, cwd=folder, env=os.environ, shell=True)

    def exit_handler():
        if os.name != 'nt':
            os.killpg(os.getpgid(preview_process.pid), signal.SIGTERM)

    atexit.register(exit_handler)


if WATCH:
    folder = FOLDER or None
    param = FOLDER if FILENAME == "main" else pj(FOLDER, FILENAME) + ".py"
    command = f"nodemon --exec {PYTHON_COMMAND} --watch {FILENAME}.py {CURRENT_FILE} {param}"
    subprocess.run(command, cwd=folder, env=os.environ, shell=True)
    exit(0)


# Run the mesh generator

env = os.environ.copy()
if USE_DOCKER:
    folder = pj(CURRENT_FOLDER, "sdf")
    command = "docker-compose run sdf"
    env["FILE"] = FILENAME + ".py"
    env["FOLDER"] = FOLDER
    subprocess.run(command, cwd=folder, env=env, shell=True)
else:
    folder = pj(CURRENT_FOLDER, FOLDER)
    command = PYTHON_COMMAND + " " + FILENAME + ".py"
    subprocess.run(command, cwd=folder, env=env, shell=True)


# Output files to the previewer

PREVIEW_FOLDER = pj(CURRENT_FOLDER, "mesh-viewer/src/assets")
PREVIEW_INFO_FILE = pj(PREVIEW_FOLDER, "info.txt")
PREVIEW_MESH_FILE = pj(PREVIEW_FOLDER, "mesh.stl")

mkdir(PREVIEW_FOLDER)
shutil.copyfile(MESH_FILE, PREVIEW_MESH_FILE)

with open(PREVIEW_INFO_FILE, "w") as f:
    id = random.randint(1000, 9999)
    f.write(f"stl {id} {PROJECT_NAME}")

if PREVIEW and not WATCH:
    command = "npm run dev"
    folder = "mesh-viewer"
    output = subprocess.Popen(command, cwd=folder, env=os.environ, shell=True)
    output.communicate()
