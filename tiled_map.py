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
 
    def render(self, screen):
        tile_count = 0
        half_width = self.tmx_data.tilewidth / 2
        half_height = self.tmx_data.tileheight / 2
        layer_count = 0
        for layer in self.tmx_data.layers:
            for column in range(self.tmx_data.width):
                for row in range(self.tmx_data.height):
                    image = self.tmx_data.get_tile_image(column, row, layer_count)
                    if image is not None and tile_count < 14:
                        #print(f"gid: {self.tmx_data.get_tile_gid(row, column, layer_count)}")
                        screen.blit(image, (cfg.X_OFFSET - 22 + (self.tmx_data.width / 2) + column * half_width - row * half_width, \
                                              cfg.Y_OFFSET + (self.tmx_data.height / 2) + row * half_height + column * half_height))
                        tile_count = tile_count + 1
            layer_count = layer_count + 1


    def make_map(self):
        print(f"width: {self.width}, height: {self.height}")
        temp_surface = pygame.Surface((self.width, self.height))
        return temp_surface
