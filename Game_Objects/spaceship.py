import pygame
from Game_Objects.base import BaseObject
from Game_Objects.bullet import Bullet
import Game_Objects.bullet
delta = 10
class Spaceship(BaseObject):
    def __init__(self,screen):
        super().__init__(screen,200,450,40,60,pygame.image.load('./Assets/ship.png'))
        self.transform()
        self.bullets=[]
        self.health=100
        
    
    def left(self):
        self.x -= delta
        if(self.x<0+self.width/2):
            self.x=0+self.width/2
     
    def right(self):
        self.x += delta
        if(self.x>(400-self.width/2)):
            self.x=400-self.width/2
    
    def down(self):
        self.y += delta
        if(self.y>600-self.height/2):
            self.y=600-self.height/2
      
    def up(self):
        self.y -= delta
        if(self.y<0+self.height/2):
            self.y=self.height/2
       
    
    def shoot(self):
        self.bullets.append(Bullet(self.screen,self.x,self.y,1))
     
    def dealDamage(self,damage):
        self.health-=damage    
    

    