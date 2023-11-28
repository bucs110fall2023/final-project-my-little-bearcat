import pygame
import time
from Doodle import Doodle
from Platforms import Platforms
from Springs import Springs
from Button import Button
menu_options = ("s", "h")

class Controller:

  def __init__(self, x, y):
  #Initialize pygame
    pygame.init()
    self.screen_width = 600
    self.screen_height = 800
    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
    pygame.display.set_caption("Allison and David's final project: Bearcat Jump")
  #Initialize objects
    # self.Doodle = Doodle (20, 20)
    # self.Platforms = Platforms()
    # self.Springs = Springs()
  

    
    
  def mainloop(self):
    #select state loop
    self.menuloop()
  
    ## below are some sample loop states ###
 
  def menuloop(self):
    while True:
      print()
      print("MENU")
      print("s = start")
      print("h = help")

      print()
      user_input = input("Please Enter an Option")
      if user_input in menu_options:
        break

      else:
        print()
        print("Option not available, pick again!")
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
def main():
  controller = Controller(20,20)
  controller.mainloop()
  pass

if __name__ == "__main__":
  main()