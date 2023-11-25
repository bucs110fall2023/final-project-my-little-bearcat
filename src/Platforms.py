import pygame
class Platforms(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image, rect) :
        super().__init__()
        self.width = 70
        self.height = 20
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("White")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    

