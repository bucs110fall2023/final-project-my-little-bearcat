import pygame
from Doodle import Doodle
from Platforms import Platforms
from Springs import Springs

class Controller:
  
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode()
    
    
  def mainloop(self):
    #select state loop
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
      #event loop
      running = True
      while running:
        for event in pygame.event.get():
          if event.type == pygame.K_SPACE:
          #move BC up
          #use set_repeat to make jump higher?
          if event.type == pygame.K_D:
          #move right
          if event.type == pygame.K_A:
          #moveleft
          if event.type == pygame.QUIT:
            running = False
          
          
           
      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw