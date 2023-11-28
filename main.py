import pygame
from Controller import Controller

def main():
    pygame.init()
    game_controller = Controller()
    game_controller.mainloop()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######
if __name__ == '__main__':
    main()
