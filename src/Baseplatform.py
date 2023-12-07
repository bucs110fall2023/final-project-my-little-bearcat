import pygame

class Baseplatform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        """
        Sets our base platform to take several different arguments
        
        Args: int - x: Top left corner coordinates on x-axis
          int - y: Top left corner coordinates on y-axis
          int - width: How wide the platform will be
          int - height: How tall the platform will  be
          str - color: color of the platform
        """
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(pygame.Color(color))
        self.rect = self.image.get_rect(topleft = (x,y))
        