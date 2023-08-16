#!/usr/bin/env bash

python3 -m PyInstaller default_pythonne.spec 

# assets_dest=dist/pythonne/assets

# python3 -m PyInstaller --onedir pythonne.py

# sudo mkdir -p $assets_dest/map
# sudo mkdir -p $assets_dest/sprites/roads

# sudo cp assets/map/* $assets_dest/map
# sudo cp assets/sprites/roads/* $assets_dest/sprites/roads
