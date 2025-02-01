import pygame

class BaseObject:
    def __init__(self,screen,x,y,width,height,image):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.image=image
        self.screen=screen
        self.rect=self.image.get_rect(center=(self.x,self.y))
    
    def transform(self):
        self.image=pygame.transform.scale(self.image,(self.width,self.height))

    def render(self):
        self.rect=self.image.get_rect(center=(self.x,self.y))
        self.screen.blit(self.image,self.rect)
       