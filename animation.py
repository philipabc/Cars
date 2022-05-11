import pygame

pygame.init()
width=350;
height=400

screen = pygame.display.set_mode( ( width, height) )
redSquare = pygame.image.load("images/red-square.png").convert()
fpsClock = pygame.time.Clock()
imageX= 200; # x coordnate of image
imageY= 30; # y coordinate of image
running = True
black = ( 0 , 0 , 0)
while (running): # loop listeneint for end of game
    imageX -= 20 ;
    screen.fill(black) # clear screen 
    screen.blit(redSquare , (imageX, imageY) ) # paint to screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    fpsClock.tick(20)
#loop over, quite pygame
pygame.quit()



