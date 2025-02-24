import pygame
import math
from Game_Objects.base import BaseObject
from Game_Objects.bullet import Bullet
class Enemies(BaseObject):
    def __init__(self,screen,x,y,respawn,fire,addBullet):
        self.screen=screen
        self.width1=80
        self.height1=40
        self.width2=86.67
        self.height2=100
        self.maxHealthSmall=3
        self.maxHealthBig=15
        self.healthSmall=self.maxHealthSmall
        self.healthBig=self.maxHealthBig
        self.x=x
        self.y=y
        self.fire=fire
        self.addBullet=addBullet
        self.theta=0
        self.image1=pygame.image.load('./Assets/enemy-medium.png')
        self.image2=pygame.image.load('./Assets/enemy-big.png')
        self.respawn=respawn
        self.bulletControl=5
        if(respawn<5):
            super().__init__(self.screen, self.x,self.y,self.width1,self.height1,self.image1)
        else:
           super().__init__(self.screen, self.x,self.y,self.width2,self.height2,self.image2)
        self.transform()
    
   
    def dealDamage(self,damage):
        if(self.respawn<5):
            self.healthSmall-=damage
        else:
            self.healthBig-=damage

        # print(self.health)
    
    def move(self):
        self.theta+=0.01
        self.y+=3
        if(self.y>=60):
            self.y=60
            if(self.theta%1<0.2):
                if(self.bulletControl==5):
                    self.addBullet(Bullet(self.screen,self.x,self.y,-1))
                    if(self.fire==1):
                        self.bulletControl=-3
                    else:
                        self.bulletControl=-10
                if(self.bulletControl<5):
                    self.bulletControl+=1
        self.x=math.sin(self.theta)*(400-self.width)/2+200
        self.render()
        self.renderHealth()

    def renderHealth(self):
        width=60
        height=7
        if(self.respawn<5):
            pygame.draw.rect(self.screen,(255,0,0), pygame.Rect(self.x-width/2, self.y-30,width ,height))
            pygame.draw.rect(self.screen,(0,200,0), pygame.Rect(self.x-width/2+1, self.y-29,(width-2)*self.healthSmall/self.maxHealthSmall ,height-2))
        else:
           pygame.draw.rect(self.screen,(255,0,0), pygame.Rect(self.x-width/2, self.y-51,width ,height))
           pygame.draw.rect(self.screen,(0,200,0), pygame.Rect(self.x-width/2+1, self.y-50,(width-2)*self.healthBig/self.maxHealthBig ,height-2))  
        return 
        

                
    