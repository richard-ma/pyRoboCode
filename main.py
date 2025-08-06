import pygame


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Python RoboCode")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Check for window close
                running = False
            if event.type == pygame.KEYDOWN: # Check for key press
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.flip()

    pygame.quit()