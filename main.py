import pygame       
from src.Controller import Controller

def main():
    pygame.init()
    game_controller = Controller(800, 600)
    game_controller.mainloop()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######
if __name__ == '__main__':
    main()
