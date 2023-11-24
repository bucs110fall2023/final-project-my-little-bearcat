import pygame
class Doodle:
    def __init__(self, image, image_path, width, height, flip, x, y):
        self.image = image
        self.flip = flip
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.flip = False
        
    def flip_direction(self, left):
        self.image = pygame.transform.flip(self.image, True, False)
        self.flip = pygame.image.load("flipped image name")