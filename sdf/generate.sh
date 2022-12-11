#!/bin/bash

INPUT=${1:-example.py}
NO_EXT=${1%.*}
OUTPUT=${2:-$NO_EXT}

cd generate
FILE=$INPUT docker-compose run sdf

cd ..
mkdir -p preview/src/assets
cp $OUTPUT.stl preview/src/assets/mesh.stl

ID=$((1 + $RANDOM % 1000))
echo "stl $ID $OUTPUT" > preview/src/assets/info.txt
