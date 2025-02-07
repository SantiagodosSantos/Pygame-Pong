from constants import *
import random
import math

class Ball():
    WIDTH = 25
    HEIGHT = 25
    X_SPEED = 5

    def __init__(self):
        self.reset()
    
    def move(self, pos = None):
        self.y -= self.y_vel
        self.x += self.x_vel
        if self.y <= 0:
            self.y_vel *= -1
            self.y = -self.y
        if self.y >= WIN_HEIGHT - self.HEIGHT:
            self.y_vel *= -1
            self.y -= self.y % (WIN_HEIGHT - self.HEIGHT)
        if pos:
            self.x, self.y = pos

    def draw(self, win):
        pygame.draw.rect(win, 'white', (self.x, self.y, self.WIDTH, self.HEIGHT))

    # def collide(self, x, y, obj):
    #     offset = (self.x - x, self.y - y)
    #     ball_mask = pygame.Mask((self.WIDTH,self.HEIGHT), True)
    #     obj_mask = pygame.Mask((obj.WIDTH, obj.HEIGHT), True)
    #     poi = ball_mask.overlap(obj_mask, offset)
    #     return poi
    
    def hit(self, obj):
        x, y = obj.x, obj.y
        offset = (self.x - x, self.y - y)
        ball_mask = pygame.Mask((self.WIDTH,self.HEIGHT), True)
        obj_mask = pygame.Mask((obj.WIDTH, obj.HEIGHT), True)
        poi = obj_mask.overlap(ball_mask, offset)
        if not poi: return
        print(poi)
        op = offset[1] -obj.HEIGHT/2 + self.HEIGHT/2
        print(op)
        if poi[0] < 2 or poi[0] > 18:
            self.x_vel *= -1
            self.y_vel = -op/50*5
        else: self.y_vel *= -1
    
    def reset(self):
        self.x = WIN_WIDTH/2
        self.y = WIN_HEIGHT/2 - self.HEIGHT/2
        self.x_vel = self.X_SPEED * random.choice([-1,1])
        self.y_vel = 0
    
    def goal(self, game_info):
        if self.x <= 0:
            game_info.score_right += 1
            self.reset()
        elif self.x >= WIN_WIDTH:
            game_info.score_left += 1
            self.reset()