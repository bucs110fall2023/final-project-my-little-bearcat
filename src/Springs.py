import pygame
class Springs:
    def __init__(self x,y):
        super().__init__()
        self.image = pygame.Surface((35, 15))
        self.image.fill("yellow")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = yield
