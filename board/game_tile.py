import pygame 

class GameTile(pygame.sprite.Sprite):
	def __init__(self, pos, image, groups):
		super().__init__(groups)
		self.image = image
		self.rect = self.image.get_rect(center = pos)
		self.pos = pygame.Vector2(pos)