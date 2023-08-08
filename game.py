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
tile_coords_dict = tile_map.get_tile_coords_dict()
grid = Grid(tile_coords_dict)

while running:

    tile_map.render(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    # get tile grid coordinates of tile covered by mouse
    highlighted_tile = grid.get_mouseover_tile()

    if highlighted_tile is not None and grid.valid_tile(highlighted_tile):
        highlight = grid.get_tile_rect(highlighted_tile)
        highlight_pts = (highlight.midleft, highlight.midtop, highlight.midright, highlight.midbottom)
        pygame.draw.lines(screen,(255, 255, 255), True, highlight_pts, 4)

    pygame.display.update()
    clock.tick(20)

pygame.quit()

