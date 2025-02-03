import Game_Objects.spaceship
import Game_Objects.enemies
import Game_Objects.bullet
import random

class Controller:
    def __init__(self, screen):
        self.respawn=int(0)
        self.screen = screen
        self.player = [Game_Objects.spaceship.Spaceship(self.screen)]
        self.enemy = [Game_Objects.enemies.Enemies(self.screen,random.randint(0,400),-50,0)]

    def tick(self):
        for i in self.player:
            i.render()
            for j in i.bullets:
                if(j.checkEnemies(self.enemy)):
                    i.bullets.remove(j)
                j.move()
            if(i.health<=0):
                self.player.remove(i)
        for i in self.enemy:
            for j in i.bullets:
                if(j.checkEnemies(self.player)):
                    i.bullets.remove(j)
            i.move()
            if(i.health<=0):
                self.enemy.remove(i)
                self.respawn+=1  
                self.enemy.append(Game_Objects.enemies.Enemies(self.screen,random.randint(0,400),-50,self.respawn))
                if(self.respawn==5):
                    self.respawn=0
            i.render()        

    def eLeft(self):
       for i in self.player:
           i.left()

    def eRight(self):
         for i in self.player:
           i.right()

    def eUp(self):
         for i in self.player:
           i.up()

    def eDown(self):
          for i in self.player:
           i.down()
    def eSpace(self):
          for i in self.player:
           i.shoot()

