import pygame
from Objects.robot import Robot

class RobotUI:
    def __init__(self, object):
        if not isinstance(object, Robot):
            raise ValueError("RobotUI requires a Robot instance")
        
        self.obj = object

    def update(self, screen):
        image = pygame.image.load("images/small.png")
        screen.blit(image, self.obj.position)