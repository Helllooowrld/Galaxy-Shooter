import Game_Objects

class Controller:
    def __init__(self, screen):
        self.screen = screen
        self.player = Game_Objects.spaceship.Spaceship(self.screen)

    def tick(self):
        self.player.render()

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

