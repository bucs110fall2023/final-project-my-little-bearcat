import pygame
import time

class BestTime:
    def __init__(self):
        self.best_time = float('inf')
        self.load_best_time()

    def update_best_time (self, current_time):
        if current_time < self.best_time:
            self.best_time = current_time
            self.save_best_time()
            
    
    def save_best_time(self):
        with open("best_time.txt", "w") as file:
            file.write(str(self.best_time))
    
    def load_best_time(self):
        try:
            with open("best_time.txt", "r") as file:
                content = file.read()
                self.best_time = float(content.strip())
                
        except (FileNotFoundError, ValueError):
            self.best_time = float('inf')
            

