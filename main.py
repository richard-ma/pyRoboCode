import pygame
import random
from pygame.math import Vector2
from Objects.movingObj import MovingObj
from Objects.bullet import Bullet
from Objects.robot import Robot
from UI.bulletUI import BulletUI


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

    for i in range(3):
        robot = Robot(name=f"Robot{i+1}")
        robot.position = Vector2(random.randint(0, screen_width), random.randint(0, screen_height))
        robot.angle = random.choice(angles)  # Random angle for the robot
        robot.stop()  # Stop the robot initially
        moving_objs.append(robot)


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
            if isinstance(moving_obj, Bullet):
                bulletUI = BulletUI(moving_obj)
                bulletUI.update(screen)
            if isinstance(moving_obj, Robot):
                image = pygame.image.load("images/small.png")
                screen.blit(image, moving_obj.position)

        pygame.display.flip()

    pygame.quit()