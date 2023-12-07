import pygame
import time

class BestTime:
    def __init__(self):
        """
        Creates a new Best Time object that keeps track of the players best time
        """
        self.best_time = "∞"
        self.best_time ='inf'
        self.load_best_time()


    def update_best_time (self, current_time):
        """
        Updates the best_time variable to the new best time
        
        Args: float - current_time: The players current time in game
        """
        if current_time < self.best_time:
            self.best_time = str(current_time)
            self.save_best_time()
            
    def save_best_time(self):
        """
        Saves the best time score to the file 'best_time.txt'
        """
        with open("best_time.txt", "w") as file:
            file.write(str(self.best_time))
    
    def load_best_time(self):
        """
        Loads the best time from the file, if the best time is not found, the best time is set to infinity
        """
        try:
            with open("best_time.txt", "r") as file:
                content = file.read()
                self.best_time = float(content.strip())
                
        except (FileNotFoundError, ValueError):
            self.best_time = float('inf')

    def print_best_time(self):
        print(f'Best Time: {self.best_time} seconds')
        