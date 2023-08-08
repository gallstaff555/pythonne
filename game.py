#!/usr/bin/env python3

import pygame
import pytmx
from tiled_map import TiledMap
from grid import Grid
from config import Config

cfg = Config()

pygame.init()
screen = pygame.display.set_mode((cfg.ROW * cfg.TILE_WIDTH, \
                                   cfg.COL * cfg.TILE_HEIGHT))
clock = pygame.time.Clock()
running = True 

tile_map = TiledMap('./assets/map/basic-map.tmx')
tile_map.render(screen)

grid = Grid()
grid.get_mouseover_tile(pygame.mouse)

tile_coords_dict = tile_map.get_tile_coords_dict()

def tileRect(tile_coords):
    x = tile_coords_dict.get(tile_coords)[0]
    y = tile_coords_dict.get(tile_coords)[1] + (cfg.ADJ_Y_OFFSET / 2)
    return pygame.Rect((x, y), (cfg.TILE_WIDTH, cfg.TILE_HEIGHT))

def valid_tile(tile_coords):
    valid = True
    if tile_coords[0] < 0 or tile_coords[0] >= cfg.COL:
        valid = False
    if tile_coords[1] < 0 or tile_coords[1] >= cfg.ROW:
        valid = False
    return valid

highlight = tileRect((0, 0))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    pygame.display.update()

    # get tile gird coordinates of tile covered by mouse
    highlighted_tile = grid.get_mouseover_tile(pygame.mouse)
    #print(f"highlighted_tile: {highlighted_tile}")

    if highlighted_tile is not None and valid_tile(highlighted_tile):
        new_highlight = tileRect(highlighted_tile)
        highlight.update(new_highlight)
        pts = [highlight.midleft, highlight.midtop, highlight.midright, highlight.midbottom]
        pygame.draw.lines(screen,(255, 255, 255), True, pts, 4)
       
    clock.tick(20)

pygame.quit()