import math
from pygame.math import Vector2


class MovingObj:
    def __init__(self):
        self.isMoving = False
        self.position = Vector2(0, 0)
        self.angle = 0

    def getNextPos(self, unit=10.0):
        if self.isMoving:
            dx = math.sin(math.radians(self.angle)) * unit
            dy = - math.cos(math.radians(self.angle)) * unit # y axis is inverted in pygame
            self.position = Vector2(self.position.x + dx, self.position.y + dy)
        return self.position