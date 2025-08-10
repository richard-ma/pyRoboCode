import pygame
from Objects.robot import Robot

class RobotUI:
    def __init__(self, object):
        if not isinstance(object, Robot):
            raise ValueError("RobotUI requires a Robot instance")
        
        self.obj = object

    def update(self, screen):
        image = pygame.image.load("images/small.png")
        image = pygame.transform.rotate(image, - self.obj.angle)
        self.obj.position = self.obj.getNextPos(unit=2.0)  # Move the robot by 2 units per update
        screen.blit(image, self.obj.position)