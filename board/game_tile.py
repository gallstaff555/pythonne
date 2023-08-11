import pygame

class GameTile(pygame.sprite.Sprite):
	def __init__(self, pos, image, groups):
		super().__init__(groups)
		self.pos = pygame.Vector2(pos)
		self.image = pygame.image.load(image).convert_alpha()
		self.rect = self.image.get_rect(center = pos)

