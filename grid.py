import pygame
from config import Config

TILE_SIZE = 32
X_OFFSET = 7
Y_OFFSET = 180

cfg = Config()

class Grid():
    def __init__(self):
        top_x = cfg.X_OFFSET
        top_y = cfg.Y_OFFSET
        
        self.map_outline = [
            pygame.math.Vector2()
        ]

    def get_mouseover_tile(self, mouse):
        x, y = mouse.get_pos()
        print(f"x:{x}, y:{y}")
        #self.iso_to_cart(x, y)

    # def mouse_to_grid(self, x, y):
    #     world_x = x - 
    # def iso_to_cart(self, mouse_x, mouse_y):
    #     cart_y = (2 * mouse_y - mouse_x) / 2
    #     cart_x = cart_y + mouse_x

    #     grid_x = int(cart_x // TILE_SIZE)
    #     grid_y = int(cart_y // TILE_SIZE)

    #     print(f"grid_x: {grid_x}, grid_y: {grid_y}")
