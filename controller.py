import Game_Objects.spaceship
import Game_Objects.enemies
import Game_Objects.bullet

class Controller:
    def __init__(self, screen):
        self.screen = screen
        self.player = Game_Objects.spaceship.Spaceship(self.screen)
        self.enemy = [Game_Objects.enemies.Enemies(self.screen)]

    def tick(self):
        self.player.render()
        
        for i in self.player.bullets:
            if(i.checkEnemies(self.enemy)):
                self.player.bullets.remove(i)
            i.move()
        for i in self.enemy:
            if(i.health<=0):
                self.enemy.remove(i)
            else:    
                i.render()
         

    def eLeft(self):
        self.player.left()

    def eRight(self):
        self.player.right()

    def eUp(self):
        self.player.up()

    def eDown(self):
        self.player.down()

    def eSpace(self):
        self.player.shoot()


