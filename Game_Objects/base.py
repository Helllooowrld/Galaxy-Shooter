import pygame

class BaseObject:
    def __init__(self,screen,x,y,width,height,image):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.image=image
        self.screen=screen

    def transform(self):
        self.image=pygame.transform.scale(self.image,(self.width,self.height))
    def render(self):
        self.screen.blit(self.image,(self.x,self.y))
    