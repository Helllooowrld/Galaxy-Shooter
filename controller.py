import Game_Objects.powerup
import Game_Objects.spaceship
import Game_Objects.enemies
import Game_Objects.bullet
import random

class Controller:
    def __init__(self, screen):
        self.refill=0
        self.score=0
        self.respawn=int(0)
        self.reappear=int(0)
        self.screen = screen
        self.player = [Game_Objects.spaceship.Spaceship(self.screen)]
        self.enemy = [Game_Objects.enemies.Enemies(self.screen,random.randint(0,400),-50,0,self.addBullet)]
        self.powerup=[Game_Objects.powerup.powerUp(self.screen,random.randint(100,360),random.randint(0,560))]
        self.bullets=[]
    
    def addBullet(self,bullet):
        self.bullets.append(bullet)

    def tick(self):
        # if(self.reappear==1):
        #     self.powerup.append(self.screen)
        self.refill=0
        self.destroy=0

        for i in self.enemy:
            # for j in i.bullets:
            #     if(j.checkEnemies(self.player)):
            #         i.bullets.remove(j)
            i.move()
            if(i.health<=0):
                self.enemy.remove(i)
                self.respawn+=1  
                self.enemy.append( Game_Objects.enemies.Enemies(self.screen,random.randint(0,400),-50,self.respawn,self.addBullet))
                if(self.respawn==5):
                    self.respawn=0
           
        self.destroy+=0.01

        for i in self.player:
            i.render()
            i.renderHealth()
            i.renderAbility(self.destroy)
            for j in i.bullets:
                if(j.checkEnemies(self.enemy)):
                    i.bullets.remove(j)
                j.move()
            if(i.health<=0):
                self.player.remove(i)

        for i in self.bullets:
            if i.checkEnemies(self.player):
               self.bullets.remove(i) 
            i.move()    

        for i in self.player:
            for k in i.bullets:
                for l in self.bullets:
                    if(k.rect.colliderect(l.rect) ):
                        i.bullets.remove(k)
                        self.bullets.remove(l)
        

            for i in self.player:
                for j in self.powerup:
                    if(j.collision(i)):
                        self.powerup.remove(j)
                        self.refill=True
                        self.reappear=0
                        self.powerup.append(Game_Objects.powerup.powerUp(self.screen,random.randint(100,360),random.randint(0,560)))
                    
                
                    if(self.reappear==500): 
            
                        j.render()
                    if(self.reappear<500):
                    
                        self.reappear+=1
        return self.refill;    
    
                
                    
                    
                    

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
    def eShift(self):
        for i in self.player:
            speed=i.shift()
        return speed
