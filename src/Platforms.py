import pygame
import random
class Platforms(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color = "white") :
        """
        Creates and initializes a platform that is displayed on the screen
        
        Args: int - x: Top left corner coordinates on the x-axis
              int - y: Top left corner coordinates on the y-axis
              int - width: How wide the platform will be
              int - height: How tall the platform will  be
              str - color: color of the platform
        """
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(pygame.Color(color))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def create_base_platform(self, screen_width):
        """
        Places a base platform at the very botom of the screen
        
        Args: int - screen_width: Width of the screen
        
        Returns: The base platform
        """
        base_platform = Platforms(0, 590, screen_width, 10, "red")
        return base_platform

    def create_platforms(num_platforms = 15):
        """
        Ramdomly generates 15 different platoforms
        
        Args: int - num_platforms: How many platforms the method should create
        
        Returns the group of platforms 
        """
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
    
    def draw (self, screen):
        """
        Draws the platoforms onto the screen
        
        Args: str - screens: Where the platforms will be shown
        """
        for platform in self.sprites():
            screen.blit(platform.image, platform.rect)