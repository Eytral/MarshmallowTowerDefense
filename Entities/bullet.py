from Constants import config, sprites
import math
import pygame

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

        # Predict where the enemy will be
        self.target_x, self.target_y = self.predict_enemy_position()

        # Compute velocity to move toward predicted position
        self.vx, self.vy = self.get_bullet_velocity()

        self.sprite = sprites.BULLET_SPRITE

        self.hitbox = pygame.Rect(self.x_pos, self.y_pos, config.GRID_CELL_SIZE//5, config.GRID_CELL_SIZE//5) # MAKE CONSTANTS FOR SIZE??

    def get_bullet_velocity(self):
        """ Compute velocity vector to move toward predicted target position. """
        dir_x = self.target_x - self.tower_x_pos #ADD CENTRE=
        dir_y = self.target_y - self.tower_y_pos

        magnitude = math.sqrt(dir_x**2 + dir_y**2)
        if magnitude == 0:  
            return 0, 0  # Avoid division by zero

        # Scale by bullet speed
        return (dir_x / magnitude) * self.speed, (dir_y / magnitude) * self.speed

    def update(self):
        """ Move the bullet and check if it reaches the target. """
        if not self.active:
            return

        self.x_pos += self.vx
        self.y_pos += self.vy
        self.hitbox = pygame.Rect(self.x_pos, self.y_pos, config.GRID_CELL_SIZE//5, config.GRID_CELL_SIZE//5) # MAKE CONSTANTS FOR SIZE??


        # Stop bullet when close to target
        if pygame.Rect.colliderect(self.target.hitbox, self.hitbox):
            self.target.take_damage(self.damage)
            self.active = False

    def draw(self, screen):
        """ Render the bullet on screen. """
        screen.blit(self.sprite, (self.x_pos, self.y_pos))

    def predict_enemy_position(self):
        """ Predict where the enemy will be when the bullet reaches it using iterative correction. """
        # Get current and previous enemy positions
        enemy_x, enemy_y = self.target.centre_position  # Current position
    # print(f"bullet think enemyx is {enemy_x} and enemy is {enemy_y}")
        prev_enemy_x, prev_enemy_y = self.target.prev_centre_position

        # Estimate enemy velocity
        enemy_vx = enemy_x - prev_enemy_x  # Change in x
        enemy_vy = enemy_y - prev_enemy_y  # Change in y

        # Distance to current enemy position
        distance = math.sqrt((enemy_x - self.tower_x_pos) ** 2 + (enemy_y - self.tower_y_pos) ** 2)
        
        # Time for bullet to reach the enemy's predicted position
        time_to_target = distance / self.speed

        # Iteratively adjust the prediction
        for _ in range(5):  # Run several iterations to refine the prediction
            # Predict enemy's future position based on its velocity
            predicted_x = enemy_x + enemy_vx * time_to_target
            predicted_y = enemy_y + enemy_vy * time_to_target

            # Calculate the distance from the tower to the predicted point
            distance = math.sqrt((predicted_x - self.tower_x_pos) ** 2 + (predicted_y - self.tower_y_pos) ** 2)
            
            # Recalculate time-to-target for the bullet to reach the new predicted position
            time_to_target = distance / self.speed

            # Update the enemy's predicted position
            enemy_x = predicted_x
            enemy_y = predicted_y

        return predicted_x, predicted_y
