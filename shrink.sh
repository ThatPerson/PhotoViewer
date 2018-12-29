#!/bin/bash

# Folder of images MUST be of the form Folder/original/*.JPG

echo "$1/final"
mkdir "$1/final"
mogrify -strip "$1/original/*.JPG"
for photos in "$1"/original/*.JPG; do
    convert "$photos" -resize 380x "${photos/original/final}"
    echo "${photos/original/final}"
done
