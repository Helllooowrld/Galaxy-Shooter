import pygame
from Game_Objects.base import BaseObject
from Game_Objects.bullet import Bullet

delta = 10
class Spaceship(BaseObject):
    def __init__(self,screen):
        super().__init__(screen,200,450,40,60,pygame.image.load('./Assets/ship.png'))
        self.transform()
        self.bullets=[]
        self.maxHealth=8
        self.health=self.maxHealth
        self.maxAbility=5
        self.ability=0.0
        self.ab=0
      
      
        
    
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
        if(self.y>567-self.height/2):
            self.y=567-self.height/2
      
    def up(self):
        self.y -= delta
        if(self.y<0+self.height/2):
            self.y=self.height/2
       
    def shoot(self):
        self.bullets.append(Bullet(self.screen,self.x,self.y,1))
    
    def shift(self):
        if self.ability <= 0.01:  
            self.ab=1
            return 1          

        if self.ability > 0:
            self.ab = 1
            return 0.5
        
       
        
     
    def dealDamage(self,damage):
        self.health-=damage  
    
    def renderHealth(self):
        width=160
        height=15
        pygame.draw.rect(self.screen,(255,0,0), pygame.Rect(400-width-20, 600-height-20,width ,height))
        pygame.draw.rect(self.screen,(0,200,0), pygame.Rect(400-width-20+2, 600-height-20+2,(width-4)*self.health/self.maxHealth ,height-4))

    def renderAbility(self,delta):
        width=160
        height=15

        # if(self.ability>=self.maxAbility):        
        #     self.ability=self.maxAbility
        #     pygame.draw.rect(self.screen,(0,0,100), pygame.Rect(400-width-20, 600-height-2,width ,height))
        #     pygame.draw.rect(self.screen,(0,0,200), pygame.Rect(400-width-20+2, 600-height-2+2,(width-4)*self.ability/self.maxAbility,height-4))
        
        if self.ab == 1:
            self.ability -= 0.02
            if self.ability < 0:  # Ensure non-negative values
                self.ability = 0

            self.ab = 0  # Reset flag

        if self.ability < self.maxAbility:
            self.ability += delta
            if self.ability > self.maxAbility:
                self.ability = self.maxAbility 

        
        
        pygame.draw.rect(self.screen,(0,0,100), pygame.Rect(400-width-20, 600-height-2,width ,height))
        pygame.draw.rect(self.screen,(0,0,200), pygame.Rect(400-width-20+2, 600-height,(width-4)*(self.ability)/self.maxAbility ,height-4))
               
                


        