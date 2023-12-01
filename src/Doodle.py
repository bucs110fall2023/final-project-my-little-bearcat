import os
import pygame

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
        original_image = pygame.image.load(image_path)

        scaled_width = 60
        scaled_height = int(original_image.get_height() * (scaled_width / original_image.get_width()))
        self.image = pygame.transform.scale(original_image, (scaled_width, scaled_height))
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 590 - scaled_height
    
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