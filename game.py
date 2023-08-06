import pygame
import pytmx
 
class TiledMap:
    def __init__(self, filename):
        self.tmx_data = pytmx.load_pygame(filename)
        self.width = self.tmx_data.width * self.tmx_data.tilewidth
        self.height = self.tmx_data.height * self.tmx_data.tileheight
 
    def render(self, surface):

        half_width = self.tmx_data.tilewidth / 2
        half_height = self.tmx_data.tileheight / 2
        layer_count = 0
        for layer in self.tmx_data.layers:
            print(f"layer:{layer}")
            for row in range(self.tmx_data.width):
                for column in range(self.tmx_data.height):
                    print(f"Row:{row}")
                    my_image = self.tmx_data.get_tile_image(row, column, layer_count)
                    print(f"image: {my_image}")
                    print(f"type:{type(my_image)}")
                    if my_image is not None:
                        screen.blit(my_image, (250 + column * half_width - row * half_width, \
                                               250 + row * half_height + column * half_height))
            layer_count = layer_count + 1

            # for x, y, image in layer.tiles():
            #     print(f"x: {x}, y:{y}, image:{image}")
            #     screen.blit(image, (x * 32, y * 32))

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