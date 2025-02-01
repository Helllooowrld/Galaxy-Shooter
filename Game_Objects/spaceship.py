import pygame
from Game_Objects.base import BaseObject
from Game_Objects.bullet import Bullet
import Game_Objects.bullet
delta = 10
class Spaceship(BaseObject):
    def __init__(self,screen):
        super().__init__(screen,50,50,40,60,pygame.image.load('./Assets/ship.png'))
        self.transform()
        self.bullets=[]
        
    
    def left(self):
        self.x -= delta
     
    def right(self):
        self.x += delta
        
    
    def down(self):
        self.y += delta
      
    def up(self):
        self.y -= delta
       
    
    def shoot(self):
        self.bullets.append(Bullet(self.screen,self.x,self.y))
     
          
    

    