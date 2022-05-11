# Simple pygame program

# Import and initialize the pygame library
# from functions import *
# from config import *
# from pygame_functions import *
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((0, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75, 2)

    # Flip the display
    pygame.display.update()

# Done! Time to quit.
pygame.quit()
