import pygame
from Game_Objects.base import BaseObject
class Enemies(BaseObject):
    def __init__(self,screen):
        self.width=80
        self.height=40
        self.health=40
        super().__init__(screen, 140,25,self.width,self.height,pygame.image.load('./Assets/enemy-medium.png'))
        self.transform()
   
    def dealDamage(self,damage):
        self.health-=damage
        print(self.health)
    