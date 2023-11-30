import pygame
class Button:
    def __init__(self, x, y, width, height, color='', text=''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        
        if self.text !='':
            font = pygame.font.SysFont('Times New Roman', 30)
            message = font.render(self.text, 1, "black",)
            screen.blit(message, (self.x + (self.width/2 - message.get_width()/2), self.y + (self.height/2 - message.get_height()/2)))

    def is_clicked(self,mouse_pos):
<<<<<<< HEAD
        return self.x < mouse_pos[0] < self.x + self.width and self.y < mouse_pos[1] < self.y +self.height
=======
         return self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y +self.height
>>>>>>> 20259a5b5a4b008515dc8e849ae5277da9120600
