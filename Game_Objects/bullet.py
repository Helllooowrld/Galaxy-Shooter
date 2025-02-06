import pygame
from Game_Objects.base import BaseObject
import Game_Objects.spaceship
delta=3
class Bullet(BaseObject):
    def __init__(self,screen,x,y,dir):
        self.screen=screen
        self.width=10
        self.height=22
        self.dir=dir
        super().__init__(screen,x,y,self.width,self.height,pygame.image.load('./Assets/laser-bolts.png'))
        self.transform()
        if(self.dir==-1):
            self.image=pygame.transform.rotate(self.image,180)
            # self.player=Game_Objects.spaceship.Spaceship(self.screen)
    
    def move(self):
        if(self.dir==-1):
            self.y+=delta
            if(self.y>=550):
                self.y=700
        else:
            self.y-=delta
        self.render()
    
     
    def collision(self,enemy):
        if(self.rect.colliderect(enemy.rect)):
            enemy.dealDamage(1)
            return True
        return False
         
    def checkEnemies(self,enemies):
        for i in enemies:
            if(self.collision(i)): return True
        return False
                