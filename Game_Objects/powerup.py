from Game_Objects.base import BaseObject
import pygame
import random
class powerUp(BaseObject):
    def __init__(self, screen,x,y,):
        self.x=x
        self.y=y
        self.image=pygame.image.load("./Assets/power-up.png") 
        super().__init__(screen,x,y,16,16, self.image)
        self.transform()
    def collision(self,player):
        if(self.rect.colliderect(player.rect)):
            return True
        else:
            return False