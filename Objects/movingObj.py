from pygame.math import Vector2


class MovingObj:
    def __init__(self):
        self.isMoving = False
        self.position = Vector2(0, 0)
        self.angle = 0

    def advance(self):
        pass