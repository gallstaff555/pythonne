import pygame
from config import Config

TILE_SIZE = 32
X_OFFSET = 7
Y_OFFSET = 180

cfg = Config()

class Grid():
    def __init__(self):
        origin = (cfg.HALF_WIDTH, 0)
        left = (0, cfg.HALF_HEIGHT)
        right = (cfg.FULL_WIDTH, cfg.HALF_HEIGHT)
        down = (cfg.HALF_WIDTH, cfg.FULL_HEIGHT)

        self.map_corners = [
            pygame.math.Vector2(origin),
            pygame.math.Vector2(right), 
            pygame.math.Vector2(left),
            pygame.math.Vector2(down)
        ]

        self.x_axis = (self.map_corners[1] - self.map_corners[0]) / cfg.COL
        self.y_axis = (self.map_corners[2] - self.map_corners[0]) / cfg.ROW

        print(f"x_axis: {self.x_axis}")
        print(f"y_axis: {self.y_axis}")

        # print("corners:")
        # print(origin)
        # print(left)
        # print(right)
        # print(down)

    def get_mouseover_tile(self, mouse):
        x, y = mouse.get_pos()
        print(f"x:{x}, y:{y}")
        #self.iso_to_cart(x, y)

    def transform(self, point, mat2x2):
        x = point[0] * mat2x2[0][0] + point[1] * mat2x2[1][0]
        y = point[0] * mat2x2[0][1] + point[1] * mat2x2[1][1]
        return pygame.math.Vector2(x, y)
    
    def test(self):
        point1 = (0,0)
        p_position1 = self.transform((point1[0] + .5, point1[1] + .5), (self.x_axis, self.y_axis)) + self.map_corners[0]
        point2 = (9,9)
        p_position2 = self.transform((point2[0] + .5, point2[1] + .5), (self.x_axis, self.y_axis)) + self.map_corners[0]
        
        print(p_position1)
        print(p_position2)
    
    
    
    
    
    
    
    
    # def mouse_to_grid(self, x, y):
    #     world_x = x - 
    # def iso_to_cart(self, mouse_x, mouse_y):
    #     cart_y = (2 * mouse_y - mouse_x) / 2
    #     cart_x = cart_y + mouse_x

    #     grid_x = int(cart_x // TILE_SIZE)
    #     grid_y = int(cart_y // TILE_SIZE)

    #     print(f"grid_x: {grid_x}, grid_y: {grid_y}")
