import os
import pygame

platforms = pygame.sprite.Group()

class Doodle(pygame.sprite.Sprite):
    def __init__(self, base_platform, platforms):
        """
        Sets up and defines our doodle class
        
        Args: Sprite - base_platform: The ground where the Doodle class will stand
              Sprite - platforms: Where doodle can jump to
        """
        super().__init__()
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.is_jumping = False
        self.is_falling = True
        self.images = []
        self.base_platform = base_platform
        self.platforms = platforms
        
        #getting image
        image_path = os.path.join("assets", "bearcatpic.jpg")
        original_image = pygame.image.load(image_path)
        self.gravity_constant = 5.0
        scaled_width = 60
        scaled_height = int(original_image.get_height() * (scaled_width / original_image.get_width()))
        self.image = pygame.transform.scale(original_image, (scaled_width, scaled_height))
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 590 - scaled_height
        
        #movement
        self.jump_height = 30
        

    def gravity(self):
        """
        Determines a gravity effect for the Doodle character, making it fall
        """
        if self.is_jumping and not self.is_falling:
            self.movey += 2.5
        elif self.rect.y < 10:
            self.movey += 2.5
        else:
            self.is_falling = True
    
    def control(self, x):
        """
        Sets how much Doodle can move right or left
        
        Args: float - x: horizontal movement
        """
        self.movex = x
    
    def jump(self):
        """
        Gives doodle a way to jump by setting how he moves up on the y-axis
        """
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_count = self.jump_height
            self.movey = -3

    def update(self):
        """
        Updates Doodle's postion(x and y), collisons, and sets boundaries on the screen 
        """
        self.rect.x += self.movex
        self.rect.y += self.movey
        self.gravity()
        
        if self.is_jumping:
            if self.jump_count >= -self.jump_height:
                self.movey = -3
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.is_falling = True
                self.movey = 3
        
        #Collisions
        collisions = pygame.sprite.spritecollide(self, self.platforms, False)
        for platform in collisions:
            if self.is_falling:
                self.rect.bottom = platform.rect.top
                self.is_falling = False
                self.is_jumping = False
                self.movey = 0
                
        base_collisions = pygame.sprite.spritecollide(self, [self.base_platform], False)
        for base in base_collisions:
            if self.is_falling:
                self.rect.y = base.rect.y - self.rect.height
                self.is_falling = False
                self.is_jumping = False
                self.movey = 0
                self.is_falling = True
        
        #Stops sliding movement
        if self.movex != 0:
            self.movex = .99 * self.movex
        
        #Boundaries        
        if self.rect.y < 0:
            self.rect.y = 0
            self.is_jumping = False
            self.is_falling = True
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 600 - self.rect.width:
            self.rect.x = 600 - self.rect.width
