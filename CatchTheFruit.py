# Catch the fruit

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from Fruit import *  # bring in the Fruit class code
from Basket import * # bring in the Basket class code
import pygwidgets

# 2 - Define constants
BLACK = (0, 0, 0)
LIME = (0, 255,0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  # set the speed (frames per second)

# 4 - Load assets: image(s), sounds, etc.
oDisplay = pygwidgets.DisplayText(window, (WINDOW_WIDTH -120, 10), '', fontSize=30)

# 5 - Initialize variables
oBasket = Basket(window, WINDOW_WIDTH, WINDOW_HEIGHT)

fruitList = []
fruitNames = ['apple', 'banana', 'cherry', 'grapes', 'pear', 'strawberry']
for fruitName in fruitNames:
    if fruitName == 'pear':
        fruitList.append(Fruit(window, WINDOW_WIDTH, WINDOW_HEIGHT, fruitName, -100))
    else:
        fruitList.append(Fruit(window, WINDOW_WIDTH, WINDOW_HEIGHT, fruitName))

oRestartButton = pygwidgets.TextButton(window, (5, 5), 'Restart')

score = 0


# 6 - Loop forever
while True:
    
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oRestartButton.handleEvent(event):  # ckicked on the Restart button
            score = 0
            for oFruit in fruitList:
                oFruit.reset()

    keyPressedList = pygame.key.get_pressed()

    if keyPressedList[pygame.K_LEFT]:  # moving left
        oBasket.move('left')

    if keyPressedList[pygame.K_RIGHT]:  # moving right
        oBasket.move('right')

    # 8 - Do any "per frame" actions
    for oFruit in fruitList:
        oFruit.update()  # tell each ball to update itself


    basketRect = oBasket.getRect()
    for oFruit in fruitList:
        fruitRect = oFruit.getRect()
        if basketRect.colliderect(fruitRect):
            nPoints = oFruit.getPoints()
            score = score + nPoints
            oFruit.reset()

    oDisplay.setValue('Score:' + str(score))

    # 9 - Clear the screen before drawing it again
    window.fill(LIME)
    
    # 10 - Draw the screen elements
    for oFruit in fruitList:
        oFruit.draw()   # tell each ball to draw itself

    oRestartButton.draw()
    oBasket.draw()
    oDisplay.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount


