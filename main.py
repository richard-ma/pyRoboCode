import pygame
import random
from pygame.math import Vector2
from pygame.sprite import Group
from Objects.movingObj import MovingObj
from Objects.bullet import Bullet
from Objects.robot import Robot
from UI.bulletUI import BulletUI
from UI.robotUI import RobotUI


if __name__ == "__main__":
    fps = 30
    screen_width, screen_height = 800, 600
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Python RoboCode")
    clock = pygame.time.Clock()

    tank_group = Group()
    for i in range(4):
        robot = Robot(name=f"Robot{i+1}")
        robot.rect.center = Vector2(random.randint(0, screen_width), random.randint(0, screen_height))
        robot.angle = [0, 90, 180, 270][i]
        robot.move()
        tank_group.add(robot)


    running = True
    while running:
        clock.tick(fps)  # Limit to 60 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Check for window close
                running = False
            if event.type == pygame.KEYDOWN: # Check for key press
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((0, 0, 0))  # Fill the screen with black

        for robot in tank_group.sprites():
            robot.angle += 45
        tank_group.update(screen=screen, clock=clock)

        pygame.display.flip()

    pygame.quit()