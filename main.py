import pygame
from pygame.math import Vector2
from Objects.bullet import *


if __name__ == "__main__":
    # This is just a placeholder for testing purposes
    print("Bullet class defined, ready for use in RoboCode simulation.")   
    bullet = Bullet(5, (255, 0, 0), None)
    for angle in [0, 90, 180, 270]:
        bullet.init(Vector2(100, 100), angle, None)
        bullet.advance()
        print("Angle:", angle, "Bullet position after advance:", bullet.getPos())
    
    # pygame.init()
    # screen = pygame.display.set_mode((800, 600))
    # pygame.display.set_caption("Python RoboCode")

    # running = True
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT: # Check for window close
    #             running = False
    #         if event.type == pygame.KEYDOWN: # Check for key press
    #             if event.key == pygame.K_ESCAPE:
    #                 running = False

    #     screen.fill((0, 0, 0))  # Fill the screen with black
    #     pygame.display.flip()

    # pygame.quit()