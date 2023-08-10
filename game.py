#!/usr/bin/env python3

# used for finding modules
import sys
sys.path.insert(0,"..")

import pygame
from config import Config
from display.tiled_map import TiledMap
from display.grid import Grid
from display.sprite_group import SpriteGroup
from display.game_tile import GameTile
import random

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

#placed_game_tiles = pygame.sprite.Group()
placed_game_tiles = SpriteGroup()
road_img = pygame.image.load('./assets/sprites/roads/road_1.png').convert_alpha()

while running:

    tile_map.render(screen)
    placed_game_tiles.draw(screen)


    # get tile grid coordinates of tile covered by mouse
    highlighted_tile = grid.get_mouseover_tile()

    # When mouse is hovering over valid tile location
    if highlighted_tile is not None and grid.valid_tile(highlighted_tile):
        highlight = grid.get_tile_rect(highlighted_tile)
        highlight_pts = (highlight.midleft, highlight.midtop, highlight.midright, highlight.midbottom)
        highlight_center = highlight.center
        pygame.draw.lines(screen,(255, 255, 255), True, highlight_pts, 4)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if highlighted_tile is not None and grid.valid_tile(highlighted_tile):
                print(f"Placing tile at {grid.get_mouseover_tile()}")
                x,y = tile_coords_dict.get(grid.get_mouseover_tile())
                x = x + (cfg.TILE_WIDTH / 2)
                y = y + cfg.TILE_HEIGHT
                random_tile = random.randint(1,12)
                new_tile = GameTile((x,y), pygame.image.load(f'./assets/sprites/roads/road_{random_tile}.png').convert_alpha(), \
                            placed_game_tiles)
                
    pygame.display.update()
    clock.tick(20)

pygame.quit()

