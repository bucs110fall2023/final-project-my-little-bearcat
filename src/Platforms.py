import pygame
class Platform(pygame.sprite.Sprite):
    def __init__ (self x,y) :
        super().__init()
        self.width = 70
        self.height = 20
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("White")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    

