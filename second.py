import pygame
import pytmx
 
class TiledMap:
    def __init__(self, filename):
        self.tmx_data = pytmx.load_pygame(filename)
        self.width = self.tmx_data.width * self.tmx_data.tilewidth
        self.height = self.tmx_data.height * self.tmx_data.tileheight
 
    def render(self, surface):

        #layer = self.tmx_data.get_layer_by_name('layer_1')
        for layer in self.tmx_data.layers:
            for x, y, image in layer.tiles():
                print(f"x: {x}, y:{y}, image:{image}")
                screen.blit(image, (x * 32, y * 32))

    def make_map(self):
        print(f"width: {self.width}, height: {self.height}")
        temp_surface = pygame.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface
    

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True 

tiled_map = TiledMap('./assets/map/basic-map.tmx')
tiled_map.make_map()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    pygame.display.update()

    clock.tick(30)

pygame.quit()