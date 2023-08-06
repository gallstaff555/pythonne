import pygame
from pytmx.util_pygame import load_pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf 
        self.rec = self.image.get_rect(topleft = pos)

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True 

tmx_data = load_pygame('./assets/map/basic-map.tmx')
sprite_group = pygame.sprite.Group()

for layer in tmx_data.layers:
    print(layer)
    for x, y, surf in layer.tiles():
        pos = (x * 32, y * 32)
        Tile(pos = pos, surf = surf, groups = sprite_group)

# get layers
# for layer in tmx_data.layers:
#     print(layer)
#tmx_data.get_layer_by_name()

#get objects 
# for obj in tmx_data.objectgroups:
#     print(obj)
#for obj in tmx_data.objects:
#   print(obj)

# get tiles 
# layer = tmx_data.get_layer_by_name("Layer_1")
# for x,y,surface in layer.tiles():
#     print(x*32)
#     print(y*32)
#     print(surface)

#layer.data

# cycle through all layers
# for layer in tmx_data.visible_layers:
# 	# if layer.name in ('Floor', 'Plants and rocks', 'Pipes')
# 	if hasattr(layer,'data'):
# 		for x,y,surf in layer.tiles():
# 			pos = (x * 32, y * 32)
# 			Tile(pos = pos, surf = surf, groups = sprite_group)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    screen.fill("purple")
    sprite_group.draw(screen)
 
    #sprite_group.draw(screen)

    # for layer in tmx_data.visible_layers:
    #     for x, y, image in layer.tiles():
    #     #image = tmx_data.get_tile_image(x, y, layer)
    #         screen.blit(image, (x * 32, y * 32))

    pygame.display.update()

    clock.tick(30)

pygame.quit()