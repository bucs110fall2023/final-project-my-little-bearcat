import pygame
import random
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
    
    def create_plateforms():
        x = random.randint(0, 600)
        y = random.randint(0, 700)
        width = 60
        height = 30
        
        return Platforms(x, y, width, height, "white")


    

