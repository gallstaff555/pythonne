import pygame
from config import Config

TILE_SIZE = 32
X_OFFSET = 7
Y_OFFSET = 180

cfg = Config()

class Grid():
    def __init__(self):
        # origin = (cfg.HALF_WIDTH, 0)
        # left = (0, cfg.HALF_HEIGHT)
        # right = (cfg.FULL_WIDTH, cfg.HALF_HEIGHT)
        # down = (cfg.HALF_WIDTH, cfg.FULL_HEIGHT)

        origin = (0, cfg.HALF_HEIGHT)
        top = (cfg.HALF_WIDTH, 0)
        right = (cfg.FULL_WIDTH, cfg.HALF_HEIGHT)
        down = (cfg.HALF_WIDTH, cfg.FULL_HEIGHT)

        self.map_corners = [
            pygame.math.Vector2(origin),
            pygame.math.Vector2(top), 
            pygame.math.Vector2(right),
            pygame.math.Vector2(down)
        ]

        self.x_axis = (self.map_corners[1] - self.map_corners[0]) / cfg.COL
        self.y_axis = (self.map_corners[3] - self.map_corners[0]) / cfg.ROW

        print(f"x_axis: {self.x_axis}")
        print(f"y_axis: {self.y_axis}")

        # print("corners:")
        # print(origin)
        # print(left)
        # print(right)
        # print(down)

    def get_mouseover_tile(self, mouse):
        (x, y) = mouse.get_pos()
        print(f"x:{x}, y:{y}")
        
        self.test()
        # point_to_grid = self.coord_to_grid((self.x_axis, self.y_axis))
        # mouse_grid_pos = self.transform(pygame.math.Vector2((x, y)) - self.map_corners[0], point_to_grid)
        # print(point_to_grid)
        # print(mouse_grid_pos)
        # print()

    def transform_to_point(self, point, mat2x2):
        x = point[0] * mat2x2[0][0] + point[1] * mat2x2[1][0]
        y = point[0] * mat2x2[0][1] + point[1] * mat2x2[1][1]
        return pygame.math.Vector2(x, y)
    
    def transform_to_grid(self, m):
        a, b, c, d = m[0].x, m[0].y, m[1].x, m[1].y
        det = 1 / (a*d - b*c)
        return [(d*det, -b*det), (-c*det, a*det)]

    def test(self):
        point1 = (9,0)
        p_position1 = self.transform_to_point((point1[0] + .5, point1[1] + .5), (self.x_axis, self.y_axis)) + self.map_corners[0]
    
        #print(f"point1: {point1}, p_position: {p_position1}")
        #print(p_position2)

        point_to_grid = self.transform_to_grid((self.x_axis, self.y_axis))
        print(point_to_grid)
        m_pos = pygame.mouse.get_pos()
        m_grid_pos = self.transform_to_point(pygame.math.Vector2(m_pos) - self.map_corners[0], point_to_grid)
        m_col, m_row = int(m_grid_pos[0]), int(m_grid_pos[1])
        print(f"m_col: {m_col}, m_row: {m_row}")

    
    
    
    
    
    
    
    # def mouse_to_grid(self, x, y):
    #     world_x = x - 
    # def iso_to_cart(self, mouse_x, mouse_y):
    #     cart_y = (2 * mouse_y - mouse_x) / 2
    #     cart_x = cart_y + mouse_x

    #     grid_x = int(cart_x // TILE_SIZE)
    #     grid_y = int(cart_y // TILE_SIZE)

    #     print(f"grid_x: {grid_x}, grid_y: {grid_y}")
