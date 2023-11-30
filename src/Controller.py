import pygame
import time
from src.Doodle import Doodle
from src.Platforms import Platforms
from src.Springs import Springs
from src.Button import Button
menu_options = ("s", "h")

class Controller:
  
  
  main = True
  

  def __init__(self, x, y):
  #Initialize pygame
    pygame.init()
    self.screen_width = 600
    self.screen_height = 800
    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
    pygame.display.set_caption("Allison and David's final project: Bearcat Jump")
    
  #Initialize objects
    self.doodle = Doodle ()
    Platforms.create_platforms()
    self.Springs = Springs(50, 70)
    self.Button = Button(50, 300, 100, 100)
    
  # For mainloop
    self.STATE = "MENU"
    self.clock = pygame.time.Clock()

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
      
      bstart = Button(50, 500, 200, 100, 'chartreuse4', 'Start Game')
      bstart.draw(self.screen)
      bquit = Button(350, 500, 200, 100, 'coral4', 'Quit')
      bquit.draw(self.screen)
      bname = Button(200, 20, 250, 100, 'cadetblue4', 'Bearcat Jump')
      bname.draw(self.screen)
      
      
      #event loop
      pygame.display.flip()
      #update data
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN:
            self.STATE = "GAME"
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
          mouse_pos = pygame.mouse.get_pos()
          if bquit.is_clicked(mouse_pos):
            running = False
      #redraw
      
      self.clock.tick(30)
      
  def gameloop(self):
      running = True
      while running:
        self.screen.fill("white")

        keys = pygame.key.get_pressed()
        if keys[pygame.K.SPACE]:
          self.doodle.jump()
        if keys[pygame.K_d]:
          self.doodle.control(10,0)
        if keys[pygame.K_a]:
          self.doodle.control(-10,0)
        
        self.doodle.update()
        self.platforms.update()
        self.springs.update()

        self.doodle.draw(self.screen)
        self.platforms.draw(self.screen)
        self.springs.draw(self.screen)

        pygame.display.flip()

        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            running = False

        self.clock.tick(30)
      #event loop
      # while running:
      #   steps = 10
      #   for event in pygame.event.get():
      #     if event.type == pygame.QUIT:
      #       running = False
      #     elif event.type == pygame.KEYDOWN:
      #       if event.key == pygame.K_SPACE:
      #         Doodle.jump()
      #       #move BC up
      #       #use set_repeat to make jump higher?
      #       elif event.key == pygame.K_d:
      #         Doodle.control(steps, 0)
      #       #move right
      #       elif event.key == pygame.K_a:
      #         Doodle.control(-steps, 0)
      #       #moveleft
      #     elif event.type == pygame.KEYUP:
      #       if event.key == pygame.K_d:
      #         Doodle.control(-steps, 0)
      #       if event.key == pygame.K_a:
      #         Doodle.control(steps, 0)
          
      #     self.screen.fill("white")
      #     pygame.display.flip()
      #     for event in pygame.event.get():
      #       if event.type == pygame.QUIT:
      #         running = False
          
      #     self.clock.tick(30)
          
        

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

if __name__ == "__main__":
  controller = Controller(20,20)
  controller.mainloop()