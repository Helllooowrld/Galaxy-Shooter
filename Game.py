import pygame  # imports pygame module
import Game_Objects
import controller
from sys import exit

import Game_Objects.spaceship  # imports exit command from sys module

pygame.init()  # initialises pygame

display = pygame.display.set_mode((512, 640))  # sets the screen display size
clock = pygame.time.Clock()  # for controlling framerate
background = pygame.image.load('Assets/River.png')  # loads image
display_font=pygame.font.Font('Assets/PixelFont1.ttf',40) #creates font
pygame.display.set_caption("Galaxy Shooter")  # sets the window name as argument
text_space=display_font.render('Space Shooter',False,'Black') #changes the font to image

def homeScreen(display):
    display.blit(background, (0, 0)) #places the surface on the display window
    display.blit(text_space,(125,50)) # places the text on the display window

gameController = controller.Controller(display)
eventSet = set()
while True:  # game loop
    for event in pygame.event.get():  # checks user inputs
        if event.type == pygame.QUIT:  # checks if the user has pressed quit button
            pygame.quit()  # quits from the game
            exit()  # exits out of the loop
        if event.type == pygame.KEYDOWN:
            eventSet.add(event.key)
        if event.type == pygame.KEYUP:
            if event.key in eventSet:
                eventSet.remove(event.key)

    for key in eventSet:
        if key == 1073741904: gameController.eLeft() 
        if key == 1073741903: gameController.eRight()
        if key == 1073741906: gameController.eUp()
        if key == 1073741905: gameController.eDown()
        if key == 32: gameController.eSpace()

    homeScreen(display)
    gameController.tick()
    pygame.display.update()  # updates the display on the basis of input given by the user
    clock.tick(60)
