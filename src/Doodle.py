import pygame
import sys
platforms = pygame.sprite.Group()
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

        bearcatpic = pygame.image.load("bearcatpic.jpg")
        bearcatpic = pygame.transform.scale(bearcatpic, (10, 10))
        self.images.append(bearcatpic)
    
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
        
        self.gravity()

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
        

        
        


