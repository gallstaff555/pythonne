#!/usr/bin/env python3

# used for finding modules
import sys
sys.path.insert(0,"..")

import pygame
from config import Config
from board.tiled_map import TiledMap
from board.grid import Grid
from board.sprite_group import SpriteGroup
from board.placed_tile import PlacedTile
from game.game import Game
from game.tiles import Tiles
import random

cfg = Config()

pygame.init()
screen = pygame.display.set_mode((cfg.ROW * cfg.TILE_WIDTH, \
                                   cfg.COL * cfg.TILE_HEIGHT))
clock = pygame.time.Clock()
running = True 

tile_map = TiledMap('./assets/map/basic-map-3.tmx')
tile_map.render(screen)
tile_coords_dict = tile_map.get_tile_coords_dict()
grid = Grid(tile_coords_dict)

# Sprite group for storing placed tiles
placed_tiles_sprite_group = SpriteGroup()
game = Game(cfg.ROW)
tiles = Tiles()

# Place first tile in center of board
first_tile = tiles.use_tile(0)
x,y = tile_coords_dict.get((8,8))
x = x + (cfg.TILE_WIDTH / 2)
y = y + cfg.TILE_HEIGHT
placed_tile = PlacedTile((x,y), f'./assets/sprites/roads/{first_tile[1]}', placed_tiles_sprite_group)

# Next playable tile setup
preview_tile_sprite_group = pygame.sprite.Group()
next_random = random.randint(1,len(tiles.get_tiles())-1) 
next_tile = tiles.preview_tile(next_random)
preview_tile = PlacedTile((50,50), f'./assets/sprites/roads/{next_tile[1]}', preview_tile_sprite_group)

while running:

    tile_map.render(screen)
    preview_tile_sprite_group.draw(screen)
    placed_tiles_sprite_group.draw(screen)


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
                tile_x,tile_y = tile_x,tile_y = grid.get_mouseover_tile()
                print(f"Placing tile at {tile_x},{tile_y}")
                x,y = tile_coords_dict.get(grid.get_mouseover_tile())
                x = x + (cfg.TILE_WIDTH / 2)
                y = y + cfg.TILE_HEIGHT
                #random_tile = random.randint(1,len(tiles.get_tiles())-1) 
                #next_tile = tiles.use_tile(next_random)
                placed_tile = PlacedTile((x,y), f'./assets/sprites/roads/{next_tile[1]}', placed_tiles_sprite_group)
                game.add_game_tile(tile_x, tile_y, placed_tile)

                next_random = random.randint(1,len(tiles.get_tiles())-1) 
                next_preview = tiles.preview_tile(next_random)
                preview_tile = PlacedTile((50,50), f'./assets/sprites/roads/{next_preview[1]}', preview_tile_sprite_group)
                next_tile = tiles.use_tile(next_random)

    pygame.display.update()
    clock.tick(20)

    if tiles.get_tile_count() < 1:
        print("No more tiles. Game over.")
        running = False

pygame.quit()

