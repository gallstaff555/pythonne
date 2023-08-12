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
from game.next_tile import NextTile
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
tile_sprite_group = SpriteGroup()
game = Game(cfg.ROW)
tiles = Tiles()
next_tile = NextTile(tiles)

preview, next = next_tile.next()
preview_tile = PlacedTile((50,50), f'./assets/sprites/roads/{preview[1]}', tile_sprite_group)

while running:

    tile_map.render(screen)
    tile_sprite_group.draw(screen)

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

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            print("Attempting to rotate left")
            next_tile.rotate_tile_left(preview)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if highlighted_tile is not None and grid.valid_tile(highlighted_tile) and game.playable(highlighted_tile):
                
                tile_x,tile_y = tile_x,tile_y = grid.get_mouseover_tile()
                print(f"Placing tile at {tile_x},{tile_y}")
                x,y = tile_coords_dict.get(grid.get_mouseover_tile())
                x = x + (cfg.TILE_WIDTH / 2)
                y = y + cfg.TILE_HEIGHT

                placed_tile = PlacedTile((x,y), f'./assets/sprites/roads/{next[1]}', tile_sprite_group)
                game.add_game_tile(tile_x, tile_y, placed_tile)
                preview, next = next_tile.next()
                preview_tile = PlacedTile((50,50), f'./assets/sprites/roads/{preview[1]}', tile_sprite_group)


    pygame.display.update()
    clock.tick(20)

    if tiles.get_tile_count() <= 1:
        print("No more tiles. Game over.")
        running = False

pygame.quit()

