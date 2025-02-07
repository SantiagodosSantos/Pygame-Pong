from constants import *

class Player():
    WIDTH = 30
    HEIGHT = 100
    SPEED = 4

    def __init__(self, left):
        self.left = left
        self.reset()
    
    def draw(self, win):
        pygame.draw.rect(win, 'white', (self.x, self.y, self.WIDTH, self.HEIGHT))

    def move_up(self):
        self.y = max(self.y - self.SPEED, 10)
    
    def move_down(self):
        self.y = min(self.y + self.SPEED, WIN_HEIGHT - self.HEIGHT - 10)
    
    def reset(self):
        self.y = WIN_HEIGHT/2 - self.HEIGHT/2
        if self.left:
            self.x = 20
        else:
            self.x = WIN_WIDTH - 20 - self.WIDTH