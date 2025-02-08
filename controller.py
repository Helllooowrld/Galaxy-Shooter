import Game_Objects.powerup
import Game_Objects.spaceship
import Game_Objects.enemies
import Game_Objects.bullet
import random
import pygame



class Controller:
    def __init__(self, screen):
        self.refill=0
        self.score=0
        self.respawn=0
        self.reappear1=0
        self.reappear2=0
        self.state=True
        self.screen = screen
        self.player = [Game_Objects.spaceship.Spaceship(self.screen)]
        self.enemy = [Game_Objects.enemies.Enemies(self.screen,random.randint(0,400),-50,0,0,self.addBullet)]
        self.powerup1=[Game_Objects.powerup.powerUp(self.screen,random.randint(100,360),random.randint(100,560),pygame.image.load("./Assets/power-up.png") )]
        self.powerup2=[Game_Objects.powerup.powerUp(self.screen,random.randint(100,360),random.randint(100,560),pygame.image.load("./Assets/health.png") )]
        self.bullets=[]
    
    def addBullet(self,bullet):
        self.bullets.append(bullet)

    def gameOver(self):
        
        return self.state  
    

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
            if(i.healthBig<=0 or i.healthSmall<=0):
                self.enemy.remove(i)
                self.respawn+=1  
                
                if(self.respawn==5):
                    self.enemy.append( Game_Objects.enemies.Enemies(self.screen,random.randint(0,400),-50,self.respawn,1,self.addBullet))
                    self.respawn=0
                else:
                    self.enemy.append( Game_Objects.enemies.Enemies(self.screen,random.randint(0,400),-50,self.respawn,0,self.addBullet))
        self.destroy+=0.01

        for i in self.player:
            for j in self.enemy:
                i.enemyCollision(j)
               

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
                self.state=False
                self.player.append(Game_Objects.spaceship.Spaceship(self.screen))
                i.health=i.maxHealth

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
                for j in self.powerup1:

                    if(j.collision(i)):
                        self.powerup1.remove(j)
                        self.refill=True
                        self.reappear1=0
                        self.powerup1.append(Game_Objects.powerup.powerUp(self.screen,random.randint(100,360),random.randint(100,560),pygame.image.load("./Assets/power-up.png") ))
                
                    if(self.reappear1==500): 
                        j.render()

                    if(self.reappear1<500):
                        self.reappear1+=1
                        
                for k in self.powerup2:
                    if(k.collision(i)):
                        self.powerup2.remove(k)
                        if(i.health<i.maxHealth):
                            i.health+=0.5
                        self.reappear2=0
                        self.powerup2.append(Game_Objects.powerup.powerUp(self.screen,random.randint(100,360),random.randint(100,560),pygame.image.load("./Assets/health.png") ))
                
                    if(self.reappear2==1000): 
                        k.render()

                    if(self.reappear2<1000):
                        self.reappear2+=1

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
