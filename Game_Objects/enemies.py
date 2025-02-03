import pygame
import math
from Game_Objects.base import BaseObject
from Game_Objects.bullet import Bullet
class Enemies(BaseObject):
    def __init__(self,screen,x,y,respawn):
        self.screen=screen
        self.width1=80
        self.height1=40
        self.width2=86.67
        self.height2=100
        self.health=40
        self.x=x
        self.y=y
        self.bullets=[]
        self.theta=0
        self.image1=pygame.image.load('./Assets/enemy-medium.png')
        self.image2=pygame.image.load('./Assets/enemy-big.png')
        self.respawn=respawn
        if(respawn<5):
            super().__init__(self.screen, self.x,self.y,self.width1,self.height1,self.image1)
        else:
           super().__init__(self.screen, self.x,self.y,self.width2,self.height2,self.image2)
        self.transform()
    
   
    def dealDamage(self,damage):
        self.health-=damage
        # print(self.health)
    
    def move(self):
        self.theta+=0.01
        if(self.theta%1<0.1):
            self.bullets.append(Bullet(self.screen,self.x,self.y,-1))
        for i in self.bullets:
            i.move()
        # if(self.y>=60):
        self.y=60
        self.x=math.sin(self.theta)*(400-self.width)/2+200   
           
        
    