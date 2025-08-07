import pygame
from Objects.bullet import Bullet

class BulletUI:
    def __init__(self, object):
        if not isinstance(object, Bullet):
            raise ValueError("BulletUI requires a Bullet instance")
        
        self.obj = object

    def update(self, screen):
        next_pos = self.obj.getNextPos(unit=5)
        pygame.draw.circle(screen, (255, 0, 0), (int(next_pos.x), int(next_pos.y)), self.obj.bsize) 