import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
gray = (180, 180, 180)
yellow = (255, 255, 0)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A car game')
clock = pygame.time.Clock()

carImg = pygame.image.load("car.jpg")
policeCar = pygame.image.load("REALpolicecar.png")
greenCar = pygame.image.load("./cars/carGREEN.png")
carImg3 = pygame.image.load("car copy.jpg")
carImg4 = pygame.image.load("car copy.jpg")


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged:"+str(count), True, red)
    gameDisplay.blit(text, (0, 0))


def otherCars(thingx, thingy, thingw, thingh, color, score):
    # pygame.draw.rect(gameDisplay, color, [thingx+130, thingy, thingw, thingh])
    if score > 49:
        gameDisplay.blit(policeCar, (thingx, thingy))
    gameDisplay.blit(greenCar, (thingx+430, thingy))
    # gameDisplay.blit(carImg3,(thingx+230,thingy))
    # gameDisplay.blit(carImg4,(thingx-130,thingy))


def road(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh], 0)


def ROAD(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh], 0)


def ROAD1(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [400, 0, 5, 800], 0)


def ROAD2(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [0, 0, 5, 800], 0)


def ROAD3(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [800, 0, 5, 800], 0)


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    # freesansbold.ttf',115)
    largeText = pygame.font.Font('font/wryh.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(20)

    game_loop()


def crash():
    message_display('You Crashed')


def game_loop():

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 3
    thing_width = 100
    thing_height = 100

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -1
                if event.key == pygame.K_RIGHT:
                    x_change = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(gray)

        #things(thingx, thingy, thingw, thingh, color)
        numbers = 30
        ROAD1(400, 0, 5, 800, black)
        for space in range(numbers):
            road(200, thing_starty+(space-numbers/2)*150, 20, 50, yellow)
            ROAD(600, thing_starty+(space-numbers/2)*150, 20, 50, yellow)
        otherCars(thing_startx, thing_starty, thing_width,
                  thing_height, black, dodged)
        ROAD1(600, thing_starty+(space-numbers/2)*150, 20, 50, black)
        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 0.1
            thing_height += (dodged * 0.1)

        if y < thing_starty+thing_height:
           #    print('y crossover')

            # police car
            # if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:#REALpolicecar
            # crash()

            # block
            # if x > thing_startx +130 and x < thing_startx+130 + thing_width or x+car_width > thing_startx+130 and x + car_width < thing_startx+130+thing_width:#REALpolicecar
            # print('x crossover')
            # crash()

            # if x > thing_startx +230 and x < thing_startx+230 + thing_width or x+car_width > thing_startx+230 and x + car_width < thing_startx+230+thing_width:#REALpolicecar
            #    # print('x crossover')
            #     crash()

            # if x > thing_startx -130 and x < thing_startx-130 + thing_width or x+car_width > thing_startx-130 and x + car_width < thing_startx-130+thing_width:#REALpolicecar
            #    # print('x crossover')
            #     crash()

            # greenCar
            if x > thing_startx + 430 and x < thing_startx+430 + thing_width or x+car_width > thing_startx+430 and x + car_width < thing_startx+430+thing_width:  # REALpolicecar
               # print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(10000)


game_loop()
pygame.quit()
quit()
