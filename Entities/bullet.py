from Constants import config, sprites

class Bullet:
    def __init__(self, x_pos, y_pos, target, speed=1, damage=1):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.target = target
        self.speed = speed
        self.damage = damage
        self.active = True  # If False, remove bullet

        self.sprite = sprites.BULLET_SPRITE

    def update(self):
        if not self.target or not self.active:
            return

        # Move towards target
        dx = self.target.position[0] - self.x_pos
        dy = self.target.position[1] - self.y_pos
        distance = (dx**2 + dy**2) ** 0.5

        if distance < self.speed:  # Bullet reached the enemy
            self.target.take_damage(self.damage)
            self.active = False
        else:
            self.x_pos += (dx / distance) * self.speed
            self.y_pos += (dy / distance) * self.speed

    def draw(self, screen):
        screen.blit(self.sprite, (self.x_pos, self.y_pos))
