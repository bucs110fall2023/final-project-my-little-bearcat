import sys
import os
import pygame

from src.Doodle import Doodle
from src.Platforms import Platforms
from src.Springs import Springs
from src.Button import Button
from src.Baseplatform import Baseplatform



class Controller:
  
  main = True

  def __init__(self, x, y):
  #Initialize pygame
    pygame.init()
    self.screen_width = 600
    self.screen_height = 600
    
    #BUTTONS
    self.bstart = Button( 50, 500, 200, 100, 'chartreuse4', 'Start Game')
    self.bquit = Button( 350, 500, 200, 100, 'cora14', 'Quit')
    self.bmenu = Button (50, 500, 200, 100, 'aquamarine4', 'Menu')
    self.brestart = Button (350, 500, 200, 100, 'chartreuse', 'Restart')
    
    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
    pygame.display.set_caption("Allison and David's final project: Bearcat Jump")
    
  #Initialize objects
    self.base_platform = Baseplatform(x=0, y=590, width=600, height = 10, color = "dark olive green")
    self.platforms = Platforms.create_platforms()
    self.doodle = Doodle (base_platform = self.base_platform, platforms = self.platforms)
    self.doodle.rect.y = self.base_platform.rect.y - self.doodle.rect.height
    self.all_sprites = pygame.sprite.Group()
    self.all_sprites.add(self.doodle, self.platforms, self.base_platform)
    
    self.button = Button(50, 300, 100, 100)
    self.all_sprites.add(self.base_platform)
  # For mainloop
    self.STATE = "MENU"
    self.clock = pygame.time.Clock()
    
  def mainloop(self):
    #select state loop
    running = True
    while running:
      if self.STATE == "MENU":
        self.menuloop()
      elif self.STATE == "GAME":
        self.gameloop()
      elif self.STATE == "GAMEOVER":
        self.gameoverloop()

  def menuloop(self):
    image = os.path.join('assets', 'blogo.jpg')
    original = pygame.image.load(image)
    background = pygame.transform.scale(original, (600, 600))
    
    running = True
    while running:
      self.screen.fill('white')
      self.screen.blit(background, (0,0))
      
      bstart = Button(50, 500, 200, 100, 'chartreuse4', 'Start Game')
      bstart.draw(self.screen)
      bquit = Button(350, 500, 200, 100, 'coral4', 'Quit')
      bquit.draw(self.screen)
      bname = Button(200, 20, 250, 100, 'cadetblue4', 'Bearcat Jump')
      bname.draw(self.screen)
      
      pygame.display.flip()
      
      #update data
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          pygame.quit()
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN:
            self.STATE = "GAME"
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
          mouse_pos = pygame.mouse.get_pos()
          if self.bquit.is_clicked(mouse_pos):
            running = False
            pygame.quit()
            sys.exit()
          if self.bstart.is_clicked(mouse_pos):
            self.STATE = "GAME"
            running = False
      
      self.clock.tick(30)
      
  def gameloop(self):
      running = True
      
      while running:
        self.screen.fill("aqua")
        
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            self.STATE = "MENU"
            running = False
           
          elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
              self.doodle.jump()
            if keys[pygame.K_d]:
              self.doodle.control(1)
            if keys[pygame.K_a]:
              self.doodle.control(-1)

        self.platforms.update()
        self.doodle.gravity()
        self.doodle.update()
        self.all_sprites.update()
        self.all_sprites.draw(self.screen)
        
        self.platforms.draw(self.screen)
        pygame.display.flip()

        if self.doodle.rect.y == 0:
          self.STATE = "GAMEOVER"
          running = False
        
        

        self.clock.tick(30)

      pygame.quit()
      sys.exit()
    
  def gameoverloop(self):
    
    running = True
    
    while running:
      self.screen.fill("black")
      bmenu = Button (50, 500, 200, 100, 'aquamarine4', 'Menu')
      bmenu.draw(self.screen)
      brestart = Button (350, 500, 200, 100, 'chartreuse', 'Restart')
      brestart.draw(self.screen)
      
      pygame.display.flip()
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
          mouse_pos = pygame.mouse.get_pos()
          if self.bmenu.is_clicked(mouse_pos):
            self.STATE = "MENU"
            running = False
          if self.brestart.is_clicked(mouse_pos):
            self.STATE = "GAME"
            running = False
      self.clock.tick(30)

      #update data

      #redraw