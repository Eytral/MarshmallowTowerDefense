from Entities.Enemies.base_enemy import Enemy
from Constants import sprites, config

class Smore(Enemy):
    def __init__(self, start_position, path, reward=5, health=10, speed=10):
        super().__init__(start_position, path, reward, health, speed)
        self.sprite = sprites.SMORE_SPRITE