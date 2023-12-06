import pygame
import random
class Platforms(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color = "white") :
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(pygame.Color(color))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def create_base_platform(self, screen_width):
        base_platform = Platforms(0, 590, screen_width, 10, "red")
        return base_platform

    def create_platforms(num_platforms = 15):
        platforms = pygame.sprite.Group()
        for _ in range (num_platforms):
            x = random.randint(0, 600)
            y = random.randint(0, 500)
            width = 50
            height = 20
            platform = Platforms(x, y, width, height, "dark olive green")
            while pygame.sprite.spritecollide(platform, platforms, False):
                platform.rect.x = random.randint(0,600)
                platform.rect.y = random.randint(0, 500)
            platforms.add(platform)
        
        return platforms
    
    #def update(self):
        #pass

    def draw (self, screen):
        for platform in self.sprites():
            screen.blit(platform.image, platform.rect)
        #for platform in self.sprites():
            #screen.blit(platform.image, platform.rect)