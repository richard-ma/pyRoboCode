import math
from pygame.math import Vector2


class MovingObj:
    def __init__(self):
        self.isMoving = False
        self.position = Vector2(0, 0)
        self.angle = 0
        self.isLocked = False

    def getNextPos(self, unit=10.0):
        if self.isMoving:
            dx = math.sin(math.radians(self.angle)) * unit
            dy = - math.cos(math.radians(self.angle)) * unit # y axis is inverted in pygame
            self.position = Vector2(self.position.x + dx, self.position.y + dy)
        return self.position

    def move(self):
        self.isMoving = True

    def stop(self):
        self.isMoving = False

    def turn(self, angle):
        if not self.isLocked:
            # Normalize the angle to be within 0-360 degrees
            self.angle = (self.angle + angle) % 360
        return self.angle
        
    def lockTurn(self):
        self.isLocked = True