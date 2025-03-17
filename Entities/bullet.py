from Constants import config, sprites
import math

class Bullet:
    def __init__(self, x_pos, y_pos, target, speed=5, damage=1):
        self.tower_x_pos = x_pos
        self.tower_y_pos = y_pos
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.target = target
        self.speed = speed
        self.damage = damage
        self.active = True  # If False, remove bullet

        # Predict where enemy will be
        self.target_x, self.target_y = self.predict_enemy_position()

        # Compute velocity to move toward predicted position
        self.vx, self.vy = self.get_bullet_velocity()

        self.sprite = sprites.BULLET_SPRITE

    def get_bullet_velocity(self):
        """ Compute velocity vector to move toward target in a straight line. """
        dir_x = self.target_x - self.tower_x_pos
        dir_y = self.target_y - self.tower_y_pos

        magnitude = math.sqrt(dir_x**2 + dir_y**2)
        if magnitude == 0:  
            return 0, 0  # Avoid division by zero
        
        return (dir_x / magnitude) * self.speed, (dir_y / magnitude) * self.speed

    def update(self):
        """ Move the bullet and check if it reaches the target. """
        if not self.active:
            return

        self.x_pos += self.vx
        self.y_pos += self.vy

        # Stop bullet when close to target
        if abs(self.x_pos - self.target_x) < 2 and abs(self.y_pos - self.target_y) < 2:
            self.target.take_damage(self.damage)
            self.active = False

    def draw(self, screen):
        """ Render the bullet on screen. """
        screen.blit(self.sprite, (self.x_pos, self.y_pos))

    def predict_enemy_position(self):
        """ Predict where the enemy will be when the bullet reaches it. """
        # Get current and previous enemy positions
        enemy_x, enemy_y = self.target.position  # Current position
        prev_enemy_x, prev_enemy_y = self.target.prev_position

        # Estimate enemy velocity
        enemy_vx = enemy_x - prev_enemy_x
        enemy_vy = enemy_y - prev_enemy_y

        # Distance to current enemy position
        distance = math.sqrt((enemy_x - self.tower_x_pos) ** 2 +
                             (enemy_y - self.tower_y_pos) ** 2)
        time_to_target = distance / self.speed  # Estimated travel time

        # Predict enemy's future position
        predicted_x = enemy_x + enemy_vx * time_to_target
        predicted_y = enemy_y + enemy_vy * time_to_target

        return predicted_x, predicted_y
