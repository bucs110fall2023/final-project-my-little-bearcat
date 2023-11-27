import pygame
class Springs:
    def __init__(self x, y, ):
        self.rect = pygame.Rect(x, y, 35, 15)
        self.image = pygame.Surface((self.rect.width, self.rect.height))
        self.image.fill("yellow")
    
