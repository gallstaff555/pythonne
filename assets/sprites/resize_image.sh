#!/bin/bash

echo "Resizing all images in given relative directory"

# sudo apt-get install imagemagick
# mogrify -resize 32x32! Image.png 

width=32
height=32

source_dir=$1

mkdir -p ${source_dir}/originals
my_files=`ls ${source_dir}/*.png`

for FILE in $my_files
do 
    mogrify -resize ${width}x${height}! $FILE
done