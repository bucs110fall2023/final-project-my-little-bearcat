import pygame
class Button:
    def __init__(self, x, y, width, height, color='', text=''):
        """
        Sets our button class to take several different arguments
        
        Args: int - x: Top left corner coordinates on the x-axis
          int - y: Top left corner coordinates on the y-axis
          int - width: How wide the button will be
          int - height: How tall the button will  be
          str - color: color of the button
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        
    def draw(self, screen):
        """
        Sets up how our button will be drawn and added to the screen
        
        Args: str - screen: where the pygame is intializing, anf therefore where the button will be
        """
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        
        if self.text !='':
            font = pygame.font.SysFont('Times New Roman', 30)
            message = font.render(self.text, 1, "black",)
            screen.blit(message, (self.x + (self.width/2 - message.get_width()/2), self.y + (self.height/2 - message.get_height()/2)))

    def is_clicked(self, mouse_pos):
        """
        Allows the computer to tell when the mouse is hovering over the button
        
        Args: touple - mouse_pos: The x and y coordinate of the mouse
        
        Returns wether or not the mouse is inside the button
        """
        return self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y +self.height
