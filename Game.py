import pygame  # imports pygame module
import Game_Objects
import controller
import Game_Objects.spaceship
from sys import exit

import Game_Objects.spaceship  # imports exit command from sys module

pygame.init()  # initialises pygame
i=1
display = pygame.display.set_mode((400, 600))  # sets the screen display size
clock = pygame.time.Clock()  # for controlling framerate
background=pygame.transform.scale(pygame.image.load('./Assets/background.png') ,(448,600))# loads image
display_font=pygame.font.Font('./Assets/PixelFont1.ttf',50) #creates font

pygame.display.set_caption("Galaxy Shooter")  # sets the window name as argument
text_space=display_font.render('Space Shooter',False,'Black') #changes the font to image
text_rect=text_space.get_rect(center=(400,50))
bullet=[(pygame.transform.scale(pygame.image.load('./Assets/laser-bolts.png') ,(15,33)))]
numOfBullets=10
bulletControl=4

background_y1=int(0)
background_y2=int(0)
bg_height=600

def homeScreen(display):
    n=numOfBullets
    display.blit(background, (0, background_y1)) #places the surface on the display window
    display.blit(background, (0, background_y2))
    for i in bullet:
        for j in range(0,n):
            display.blit(i,(0+20*j,567))
            j+=1
        


        

gameController = controller.Controller(display)
eventSet = set()
while True:  # game loop
    speed=int(1)
    player=Game_Objects.spaceship.Spaceship(display)
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
        if key == 32: 
            if(numOfBullets>=1 and bulletControl==4):
                gameController.eSpace()
                numOfBullets-=1
                bulletControl=-5
            if(bulletControl<4):
                bulletControl+=1
            
           
        if key== 1073742049 or key==1073742053:
            speed=gameController.eShift()

   
    if i==1:
        background_y1+=2
        if background_y1>bg_height:
            background_y1=background_y2-bg_height
        background_y2=background_y1-bg_height
        i=0
    else:
        background_y2+=2
        background_y1+=2
        if background_y1>bg_height:
            background_y1=background_y2-bg_height
        if background_y2>bg_height:
            background_y2=background_y1-bg_height

    
    
    homeScreen(display)
    refill=gameController.tick()
    if(refill==True):
        if(numOfBullets<10):
            numOfBullets+=1
    pygame.display.update()  # updates the display on the basis of input given by the user
    print(speed)
    clock.tick(60*speed)
