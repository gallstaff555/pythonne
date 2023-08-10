#!/usr/bin/env python3

import pygame
import pytmx
from tiled_map import TiledMap
from grid import Grid
from config import Config
from game_tile import GameTile

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

placed_game_tiles = pygame.sprite.Group()
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
                print(grid.get_mouseover_tile())
                x,y = tile_coords_dict.get(grid.get_mouseover_tile())
                x = x + (cfg.TILE_WIDTH / 2)
                y = y + cfg.TILE_HEIGHT
                print(pygame.mouse.get_pos())
                new_tile = GameTile((x,y), road_img, placed_game_tiles)
                
    pygame.display.update()
    clock.tick(20)

pygame.quit()

