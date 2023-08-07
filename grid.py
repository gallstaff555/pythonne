import pygame
from config import Config

cfg = Config()

class Grid():
    def __init__(self):
        self.origin = (cfg.HALF_WIDTH, 0)
        self.left = (0, cfg.HALF_HEIGHT)
        self.right = (cfg.FULL_WIDTH, cfg.HALF_HEIGHT)
        self.down = (cfg.HALF_WIDTH, cfg.FULL_HEIGHT)

        #define outer corners of grid
        self.map_corners = [
            pygame.math.Vector2(self.origin),
            pygame.math.Vector2(self.left), 
            pygame.math.Vector2(self.right),
            pygame.math.Vector2(self.down)
        ]

        self.x_axis = (self.map_corners[2] - self.origin) / cfg.COL
        self.y_axis = (self.map_corners[1] - self.origin) / cfg.ROW

    # Display tile currently moused over
    def get_mouseover_tile(self, mouse):
        point_to_grid = self.get_point_to_grid((self.x_axis, self.y_axis))
        mouse_pos = pygame.mouse.get_pos()
        mouse_grid_pos = self.transform_to_point(pygame.math.Vector2(mouse_pos) - self.origin, point_to_grid)
        mouse_col, mouse_row = int(mouse_grid_pos[0]), int(mouse_grid_pos[1])
        return (mouse_col, mouse_row)
        
    # Convert tile coordinates to mouse coordinate
    def transform_to_point(self, point, mat2x2):
        x = point[0] * mat2x2[0][0] + point[1] * mat2x2[1][0]
        y = point[0] * mat2x2[0][1] + point[1] * mat2x2[1][1]
        return pygame.math.Vector2(x, y)
    
    # Conversion for mouse coord to tile coord
    def get_point_to_grid(self, axes):
        a, b, c, d = axes[0].x, axes[0].y, axes[1].x, axes[1].y
        det = 1 / (a*d - b*c)
        return [(d*det, -b*det), (-c*det, a*det)]
        

    
