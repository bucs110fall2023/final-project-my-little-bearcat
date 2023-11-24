import pygame
class Doodle:
    def __init__(self, image, flip, x, y):
        self.image = image
        self.flip = flip
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        
    def flip_direction(self, left):
        self.flip = pygame.image.load("flipped image name")