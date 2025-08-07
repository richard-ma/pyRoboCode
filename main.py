import pygame
import random
from pygame.math import Vector2
from Objects.bullet import *


if __name__ == "__main__":
    fps = 30
    screen_width, screen_height = 800, 600
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Python RoboCode")

    # all moving objects list
    moving_objs = []

    angles = [0, 45, 90, 135, 180, 225, 270, 315]
    for i in range(8):  # Create 5 bullets for demonstration
        bullet = Bullet(power=9, bot=None)  # Assuming bot is not used in this context
        bullet.position = Vector2(screen_width//2, screen_height//2)  # Start in the center of the screen
        bullet.isMoving = True
        bullet.angle = angles[i]  # Set an angle for the bullet
        moving_objs.append(bullet) # append the bullet to the moving objects list


    running = True
    while running:
        pygame.time.Clock().tick(fps)  # Limit to 60 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Check for window close
                running = False
            if event.type == pygame.KEYDOWN: # Check for key press
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((0, 0, 0))  # Fill the screen with black

        for moving_obj in moving_objs:
            if isinstance(moving_obj, MovingObj):
                next_pos = moving_obj.getNextPos(unit=5)
                pygame.draw.rect(screen, (255, 0, 0), (next_pos.x, next_pos.y, bullet.bsize, bullet.bsize))

        pygame.display.flip()

    pygame.quit()