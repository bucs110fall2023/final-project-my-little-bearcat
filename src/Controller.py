import sys
import os
import pygame

from src.Doodle import Doodle
from src.Platforms import Platforms
#from src.Springs import Springs
from src.Button import Button
from src.Baseplatform import Baseplatform
from src.BestTime import BestTime

class Controller:
  
  main = True

  def __init__(self, x, y):
    """
    Creates a new controller object
    
    Args: int - x: How wide the window will be
          int - y: How tall the window will be
    """
  #Initialize pygame
    pygame.init()
    self.screen_width = 600
    self.screen_height = 600
    self.font = pygame.font.Font(None, 36)
    
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
    self.timer = 0
    self.best_time_manager = BestTime()
    self.button = Button(50, 300, 100, 100)
    self.all_sprites.add(self.base_platform)
    
  # For mainloop
    self.STATE = "MENU"
    self.clock = pygame.time.Clock()
    
  def mainloop(self):
    """
    Manages the different game states
    """
    #selecting a state loop
    running = True
    while running:
      if self.STATE == "MENU":
        self.menuloop()
      elif self.STATE == "GAME":
        self.gameloop()
      elif self.STATE == "GAMEOVER":
        self.gameoverloop()

  def menuloop(self):
    """
    A loop that controls the menu state
    """
    image = os.path.join('assets', 'blogo.jpg')
    original = pygame.image.load(image)
    background = pygame.transform.scale(original, (600, 600))
    
    running = True
    while running:
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
    """
    A loop for controling the game state
    """
    running = True
      
    while running:
      self.timer += self.clock.tick(30)/1000.0
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
      #font = pygame.font.Font(None, 36)
      text = self.font.render(f'Time: {int(self.timer)} seconds', True, "black")
      best_time_text = self.font.render(f'Best Time: {int(self.best_time_manager.best_time)} seconds', True, "black")
      self.screen.blit(text, (10, 10))
      self.screen.blit(best_time_text, (10, 50))

      pygame.display.flip()

      if self.doodle.rect.y == 0:
        self.best_time_manager.save_best_time()
        self.STATE = "GAMEOVER"
        running = False
    self.clock.tick(30)

  def gameoverloop(self):
    """
    A loop that controls the game over state
    """
    running = True
    
    while running:
      #Screen set up
      self.screen.fill("blanchedalmond")
      bmenu = Button (50, 500, 200, 100, 'darkolivegreen3', 'Menu')
      bmenu.draw(self.screen)
      brestart = Button (350, 500, 200, 100, 'darkorange3', 'Restart')
      brestart.draw(self.screen)
      
      
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
          mouse_pos = pygame.mouse.get_pos()
          if self.bmenu.is_clicked(mouse_pos):
            self.STATE = "MENU"
            running = False
          if self.brestart.is_clicked(mouse_pos):
            self.reset_game()
            self.STATE = "GAME"
            running = False
      text = self.font.render(f'Time: {int(self.timer)} seconds', True, "white")
      best_time_text = self.font.render(f'Best Time: {int(self.best_time_manager.best_time)} seconds', True, "white")
      self.screen.blit(text, (10, 10))
      self.screen.blit(best_time_text, (10, 50))

      self.clock.tick(30)
    pygame.display.flip()

  def reset_game(self):
    """
    Resets the game to get ready for a new one
    """
    
    self.timer = 0
    
    self.best_time_manager.save_best_time()
    self.best_time_manager.load_best_time()
    self.base_platform = Baseplatform(x=0, y = 590, width = 600, height = 10, color = "dark olive green")
    self.platforms = Platforms.create_platforms()
    self.doodle = Doodle(base_platform = self.base_platform, platforms = self.platforms)
    self.doodle.rect.y = self.base_platform.rect.y - self.doodle.rect.height
    self.all_sprites = pygame.sprite.Group()
    self.all_sprites.add(self.doodle, self.platforms, self.base_platform)
    self.STATE = "GAME"

    self.screen.fill("aquamarine4")
    font = pygame.font.Font(None, 36)
    best_time_text = font.render(f'Best Time: {int(self.best_time_manager.best_time)} seconds', True, "black")
    self.screen.blit(best_time_text, (10, 50))
    pygame.display.flip()
    
    
    self.gameloop()

    