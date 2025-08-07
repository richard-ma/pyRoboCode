import pygame
from pygame.math import Vector2
from Objects.bullet import *


if __name__ == "__main__":
    fps = 30
    screen_width, screen_height = 800, 600
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Python RoboCode")

    width, height = 50, 50
    centerx, centery = screen.get_width() // 2, screen.get_height() // 2
    rect = pygame.Rect((centerx-width//2, centery-height//2), (width, height))
    bullet = Bullet(power=5, bot=None)  # Assuming bot is not used in this context
    bullet.position = Vector2(centerx, centery)
    bullet.isMoving = True

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
        bullet.angle = 45  # Set an angle for the bullet
        next_pos = bullet.getNextPos()  # Get the next position of the bullet
        pygame.draw.rect(screen, (255, 0, 0), (next_pos.x, next_pos.y, bullet.bsize, bullet.bsize))
        pygame.display.flip()

    pygame.quit()