import pygame
from Doodle import Doodle
from Platforms import Platforms
from Springs import Springs

class Controller:

  def __init__(self, x, y):
  #Initialize pygame
    pygame.init()
    self.screen_width = 600
    self.screen_height = 800
    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
    pygame.display.set_caption("Allison and David's final project: Bearcat Jump")
    self.screen = pygame.display.set_mode()
  #Initialize objects
    self.Doodle = Doodle(self.screen_width, self.screen_height)
    self.platforms = Platforms()
    
    
  def mainloop(self):
    #select state loop
    pass
  
    ## below are some sample loop states ###

  def menuloop(self):
    
      #event loop
      # self.screen.fill("aquamarine")

      #update data

      #redraw
    pass
  def gameloop(self):
      #event loop
      running = True
      while running:
        for event in pygame.event.get():
          if event.type == pygame.QUIT():
            running = False
          elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
              pass
            #move BC up
            #use set_repeat to make jump higher?
            elif event.type == pygame.K_D:
              pass
            #move right
            elif event.type == pygame.K_A:
              pass
            #moveleft
          

      #update data

      #redraw
    
  def gameoverloop(self):
    pass
      #event loop

      #update data

      #redraw
def main():
  pass

if __name__ == "__main__":
  main()