import pygame
import pytmx
from config import Config

cfg = Config()
 
class TiledMap:
    def __init__(self, filename):
        self.tmx_data = pytmx.load_pygame(filename)
        self.width = self.tmx_data.width * self.tmx_data.tilewidth
        self.height = self.tmx_data.height * self.tmx_data.tileheight
        self.total_tiles = self.tmx_data.width * self.tmx_data.height
        self.tile_coords_dict = {}
 
    # Render each tile in every layer
    def render(self, screen):
        layer_count = 0
        for layer in self.tmx_data.layers:
            for column in range(self.tmx_data.width):
                for row in range(self.tmx_data.height):
                    image = self.tmx_data.get_tile_image(column, row, layer_count)
                    if image is not None:
                        # Pattern for isometric tiles
                        x_coord = cfg.X_OFFSET - cfg.ADJ_Y_OFFSET + (cfg.ROW / 2) + column * (cfg.TILE_WIDTH / 2) - row * (cfg.TILE_WIDTH / 2)
                        y_coord = cfg.Y_OFFSET + (cfg.COL / 2) + row * (cfg.TILE_HEIGHT / 2) + column * (cfg.TILE_HEIGHT / 2)
                        if layer_count == 0:
                            self.tile_coords_dict[(column, row)] = (x_coord, y_coord)
                        screen.blit(image, (x_coord, y_coord))
                       
            layer_count = layer_count + 1

    def get_tile_coords_dict(self):
        return self.tile_coords_dict



