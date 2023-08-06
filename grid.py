import pygame
from config import Config

TILE_SIZE = 32
X_OFFSET = 7
Y_OFFSET = 180

cfg = Config()

class Grid():
    def __init__(self):
        self.origin = (cfg.HALF_WIDTH, 0)
        self.left = (0, cfg.HALF_HEIGHT)
        self.right = (cfg.FULL_WIDTH, cfg.HALF_HEIGHT)
        self.down = (cfg.HALF_WIDTH, cfg.FULL_HEIGHT)

        # origin at left
        # self.orgin = (0, cfg.HALF_HEIGHT)
        # top = (cfg.HALF_WIDTH, 0)
        # right = (cfg.FULL_WIDTH, cfg.HALF_HEIGHT)
        # down = (cfg.HALF_WIDTH, cfg.FULL_HEIGHT)

        self.map_corners = [
            pygame.math.Vector2(self.origin),
            pygame.math.Vector2(self.left), 
            pygame.math.Vector2(self.right),
            pygame.math.Vector2(self.down)
        ]

        self.x_axis = (self.map_corners[2] - self.origin) / cfg.COL
        self.y_axis = (self.map_corners[1] - self.origin) / cfg.ROW


        # origin at self.left
        # self.x_axis = (self.map_corners[1] - self.map_corners[0]) / cfg.COL
        # self.y_axis = (self.map_corners[3] - self.map_corners[0]) / cfg.ROW


        print(f"x_axis: {self.x_axis}")
        print(f"y_axis: {self.y_axis}")

        # print("corners:")
        # print(self.orgin)
        # print(self.left)
        # print(right)
        # print(down)

    def get_mouseover_tile(self, mouse):
        point_to_grid = self.get_point_to_grid((self.x_axis, self.y_axis))
        m_pos = pygame.mouse.get_pos()
        m_grid_pos = self.transform_to_point(pygame.math.Vector2(m_pos) - self.origin, point_to_grid)
        m_col, m_row = int(m_grid_pos[0]), int(m_grid_pos[1])
        print(f"m_col: {m_col}, m_row: {m_row}")
        

    def transform_to_point(self, point, mat2x2):
        x = point[0] * mat2x2[0][0] + point[1] * mat2x2[1][0]
        y = point[0] * mat2x2[0][1] + point[1] * mat2x2[1][1]
        return pygame.math.Vector2(x, y)
    
    def get_point_to_grid(self, axes):
        a, b, c, d = axes[0].x, axes[0].y, axes[1].x, axes[1].y
        det = 1 / (a*d - b*c)
        return [(d*det, -b*det), (-c*det, a*det)]

    def test(self):
        point1 = (9,0)
        p_position1 = self.transform_to_point((point1[0] + .5, point1[1] + .5), (self.x_axis, self.y_axis)) + self.origin
    
        #print(f"point1: {point1}, p_position: {p_position1}")
        #print(p_position2)

        

    
    
    
    
    
    
    
    # def mouse_to_grid(self, x, y):
    #     world_x = x - 
    # def iso_to_cart(self, mouse_x, mouse_y):
    #     cart_y = (2 * mouse_y - mouse_x) / 2
    #     cart_x = cart_y + mouse_x

    #     grid_x = int(cart_x // TILE_SIZE)
    #     grid_y = int(cart_y // TILE_SIZE)

    #     print(f"grid_x: {grid_x}, grid_y: {grid_y}")
