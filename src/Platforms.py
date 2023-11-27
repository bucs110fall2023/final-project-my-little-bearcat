import pygame
class Platforms(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color = "white") :
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(pygame.Color(color))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    

