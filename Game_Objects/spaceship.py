import pygame
from Game_Objects.base import BaseObject
delta = 10

class Spaceship(BaseObject):
    def __init__(self,screen):
        super().__init__(screen,0,0,50,75,pygame.image.load('./Assets/ship.png'))
        self.transform()
    
    def left(self):
        self.x -= delta

    def right(self):
        self.x += delta
    
    def down(self):
        self.y += delta
    
    def up(self):
        self.y -= delta
    
    def shoot(self):
        print("shooot")