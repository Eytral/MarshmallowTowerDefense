from Entities.Enemies.base_enemy import Enemy
from Constants import sprites, config

class WhiteChocolate(Enemy):
    def __init__(self, start_position, path):
        super().__init__(start_position, path)
        self.sprite = sprites.WHITE_CHOCOLATE_SPRITE