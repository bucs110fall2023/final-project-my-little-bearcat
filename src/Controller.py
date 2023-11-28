import pygame
import time
from Doodle import Doodle
from Platforms import Platforms
from Springs import Springs
from Button import Button
menu_options = ("s", "h")

class Controller:

  clock = pygame.time.Clock()
  main = True
  

  def __init__(self, x, y):
  #Initialize pygame
    pygame.init()
    self.screen_width = 600
    self.screen_height = 800
    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
    pygame.display.set_caption("Allison and David's final project: Bearcat Jump")
  #Initialize objects
    self.Doodle = Doodle (20, 20)
    self.Platforms = Platforms()
    self.Springs = Springs()
    self.Button = Button()
  # For mainloop
    self.STATE = "MENU"
    
  def mainloop(self):
    #select state loop
    while True:
      if self.STATE == "MENU":
        self.menuloop()
      elif self.STATE == "GAME":
        self.gameloop()
      elif self.STATE == "GAMEOVER":
        self.gameoverloop()
    ## below are some sample loop states ###
 
  def menuloop(self):
    while True:
      self.screen.fill('white')
      b = Button(50, 300, 100, 100, 'red', 'Start Game')
      b.draw(self.screen)
      #event loop

      #update data

      #redraw
      pygame.display.flip()
      pygame.time.wait(1000)
      
  def gameloop(self):
      self.flipped = not self.flipped
      #event loop
      running = True
  
      while running:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            running = False
          elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
              pass
            #move BC up
            #use set_repeat to make jump higher?
            elif event.key == pygame.K_d:
              pass
            #move right
            elif event.key == pygame.K_a:
              pass
            #moveleft
          
        self.screen.fill("white")
        pygame.display.flip()
        

      #update data

      #redraw
    
  def gameoverloop(self):
    pass
      #event loop

      #update data

      #redraw
#def main():
  #controller = Controller(20,20)
  #controller.mainloop()
  #pass

#if __name__ == "__main__":
  #main()