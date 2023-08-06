#!/usr/bin/env python3

import pygame
#import pytmx
from tiled_map import TiledMap
from grid import Grid
from config import Config

cfg = Config()

pygame.init()
screen = pygame.display.set_mode((cfg.TILE_ROW * cfg.TILE_WIDTH, \
                                   cfg.TILE_COL * cfg.TILE_HEIGHT))
clock = pygame.time.Clock()
running = True 

background = TiledMap('./assets/map/basic-map-2.tmx')
background.make_map()
background.render(screen)

grid = Grid()
grid.get_mouseover_tile(pygame.mouse)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    pygame.display.update()
    grid.get_mouseover_tile(pygame.mouse)

    clock.tick(1)

pygame.quit()