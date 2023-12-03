import os
import pygame

platforms = pygame.sprite.Group()

class Doodle(pygame.sprite.Sprite):
    def __init__(self, base_platform):
        super().__init__()
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.is_jumping = False
        self.is_falling = True
        self.images = []
        self.velocity = 0
        self.base_platform = base_platform
        #getting image
        image_path = os.path.join("assets", "bearcatpic.jpg")
        original_image = pygame.image.load(image_path)

        scaled_width = 60
        scaled_height = int(original_image.get_height() * (scaled_width / original_image.get_width()))
        self.image = pygame.transform.scale(original_image, (scaled_width, scaled_height))
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 590 - scaled_height

        self.jump_height = 70
        

    def gravity(self):
        if self.is_jumping:
            self.movey +=3.0
    
    def control(self, x, y):
        self.movex += x
    
    def jump(self):
        
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_count = self.jump_height

    def update(self):
    
        
        if self.is_jumping:
            if self.jump_count >= -self.jump_height:
                self.rect.y -= (self.jump_count*abs(self.jump_count))*0.5
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.is_falling = True
            
        collisions = pygame.sprite.spritecollide(self, platforms, False)
        for platform in collisions:
            if self.is_falling:
                self.rect.y = platform.rect.y - self.rect.height
                self.is_falling = False
                self.is_jumping = False
                

        base_collisions = pygame.sprite.spritecollide(self, [self.base_platform], False)
        for base in base_collisions:
            if self.is_falling:
                self.rect.y = base.rect.y - self.rect.height
                self.is_falling = False
                self.is_jumping = False
                
        if self.movex < 0:
            self.image = pygame.transform.flip(self.images [0], True, False)
        if self.movex > 0:
            self.image = self.images[0]