import pygame
import pytmx
 
class TiledMap:
    def __init__(self, filename):
        self.tmx_data = pytmx.load_pygame(filename)
        self.width = self.tmx_data.width * self.tmx_data.tilewidth
        self.height = self.tmx_data.height * self.tmx_data.tileheight
 
    def render(self):

        half_width = self.tmx_data.tilewidth / 2
        half_height = self.tmx_data.tileheight / 2
        layer_count = 0
        for layer in self.tmx_data.layers:
            print(f"layer:{layer}")
            for row in range(self.tmx_data.width):
                for column in range(self.tmx_data.height):
                    image = self.tmx_data.get_tile_image(row, column, layer_count)
                    if image is not None:
                        screen.blit(image, (250 + (self.tmx_data.width / 2) + column * half_width - row * half_width, \
                                               (self.tmx_data.height / 2) + row * half_height + column * half_height))
            layer_count = layer_count + 1

    def make_map(self):
        print(f"width: {self.width}, height: {self.height}")
        temp_surface = pygame.Surface((self.width, self.height))
        return temp_surface

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True 

background = TiledMap('./assets/map/basic-map.tmx')
background.make_map()
background.render()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    pygame.display.update()

    clock.tick(30)

pygame.quit()