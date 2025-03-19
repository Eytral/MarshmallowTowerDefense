from Entities.Enemies.base_enemy import Enemy
from Constants import sprites, config

class Marshmallow(Enemy):
    def __init__(self, start_position, path):
        super().__init__(start_position, path)
        self.sprite = sprites.MARSHMALLOW_SPRITE