class Doodle:
    def __init__(self, image, flip, x, y):
        self.image = image
        self.flip = flip
        self.x = x
        self.y = y
        
    def flip_direction(self, left):
        self.flip = pygame.image.load("flipped image name")