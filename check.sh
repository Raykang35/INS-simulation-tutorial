#!/bin/bash
### This is to check all calculations were finished. ###
for folder in */; do
    if [ ! -e "$folder/vasprun.xml" ]; then
        echo "File not found in folder: $folder"
    fi
done

echo "Finish checking"
