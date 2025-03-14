from Constants import sprites, config

class Enemy():
    def __init__(self, reward, health, speed, position, path):
        self.reward = reward
        self.health = health
        self.speed = speed
        self.position = position
        self.path = path
        self.is_dead = False
        self.sprite = sprites.ENEMY_DEFAULT_SPRITE
        
    def move(self):
        for target_position in self.path:
            if self.position != target_position:

                x1, y1 = self.position
                x2, y2 = target_position
                
                # Move horizontally
                if x1 < x2:
                    x1 += 1
                elif x1 > x2:
                    x1 -= 1
                
                # Move vertically
                if y1 < y2:
                    y1 += 1
                elif y1 > y2:
                    y1 -= 1
                
                # Update the enemy's position
                self.position = (x1, y1)


    def draw(self, screen):
        screen.blit(self.sprite, (self.position))

    def take_damage(self):
        self.health -= 1

    def check_is_dead(self):
        if self.health >= 0:
            self.is_dead = True

    def update(self):
        self.check_is_dead()
        self.take_damage()
        self.move()
        