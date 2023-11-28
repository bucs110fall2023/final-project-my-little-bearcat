import pygame
import sys

class Doodle:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.health = 10
        self.is_jumping = False
        self.is_falling = True
        self.images = []

        bearcatpic = pygame.image.load(bearcatpic.jpg)
    
    def gravity(self):
        if self.is_jumping:
            self.movey +=3.0
    
    def control(self, x, y):
        self.movex += x
    
    def jump(self):
        if self.is_jumping is False:
            self.is_falling = False
            self.is_jumping = True

    def update(self):
        #moving left
        if self.movex < 0:

    # def __init__(self, image, image_path, width, height, flip, x, y):
    #     self.image_path = image_path
    #     # self.flip = flip
    #     self.x = x
    #     self.y = y
    #     self.width = width
    #     self.height = height
    #     self.image = pygame.image.load(image_path)
    #     self.image = pygame.transform.scale(self.image, (width, height))
    #     self.flip = False
        
#    def flip_direction(self, left):
#         self.image = pygame.transform.flip(self.image, True, False)
#         self.flipped = not self.flipped