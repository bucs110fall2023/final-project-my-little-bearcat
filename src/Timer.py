import pygame
import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.highest_score = 0
    
    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self):
        if self.start_time is not None:
            self.end_time = time.time()
            elapsed_time = self.end_time - self.start_time
            self.update_highest_score (elapsed_time)
            self.start_time = None
    
    def update_highest_score(self, elapsed_time):
        current_score = int(elapsed_time)
        if current_score > self.highest_score:
            self.highest_score = current_score
    def get_elapsed_time(self):
        if self.start_time is not None and self.end_time is not None:
            elapsed_time = self.end_time - self.start_time
            return elapsed_time
        else:
            return 0
    def get_highest_score(self):
        return self.highest_score
