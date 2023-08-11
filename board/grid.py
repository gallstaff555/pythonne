import pygame
from config import Config

cfg = Config()

class Grid():
    def __init__(self, tile_coords_dict):
        self.tile_coords_dict = tile_coords_dict
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
    def get_mouseover_tile(self):
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
    
    # Convert tile coords to raw coords and return a rect at that coordinate
    def get_tile_rect(self, tile_coords):
        x = self.tile_coords_dict.get(tile_coords)[0]
        y = self.tile_coords_dict.get(tile_coords)[1] + (cfg.ADJ_Y_OFFSET / 2)
        return pygame.Rect((x, y), (cfg.TILE_WIDTH, cfg.TILE_HEIGHT))

    # A valid tile falls within the bounds of the tile map
    def valid_tile(self, tile_coords):
        return not (tile_coords[0] < 0 or tile_coords[0] >= cfg.COL) \
            and not (tile_coords[1] < 0 or tile_coords[1] >= cfg.ROW)
        

    
