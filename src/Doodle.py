import os
import pygame
import sys

platforms = pygame.sprite.Group()

class Doodle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.is_jumping = False
        self.is_falling = True
        self.images = []
        self.velocity = 0
        
        #getting image
        image_path = os.path.join("assets", "bearcatpic.jpg")
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
    
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
        self.velocity += 1
        self.rect.y += self.velocity

        if self.rect.top > (900):
            self.rect.bottom = 0
        

        collisions = pygame.sprite.spritecollide(self, platforms, False)
        for platform in collisions:
            if self.is_falling:
                self.rect.y = platform.rect.y - self.rect.height
                self.is_falling = False
                self.is_jumping = False
                self.movey = 0
        if self.movex < 0:
            self.image = pygame.transform.flip(self.images [0], True, False)
        if self.movex > 0:
            self.image = self.images[0]