from Constants import sprites, config
import copy

class Enemy():
    def __init__(self, start_position, path, reward=5, health=10, speed=1):
        self.reward = reward
        self.health = health
        self.speed = speed
        self.position = start_position
        self.path = copy.deepcopy(path)
        self.is_dead = False
        self.reached_end = False
        self.sprite = sprites.ENEMY_DEFAULT_SPRITE
        
    def move(self):
        target_position = self.path[0]
        #print(f"targeting positiong: {target_position}")

        x1, y1 = self.position
        x2, y2 = target_position
        
        # Move horizontally
        if x1 < x2:
            x1 += self.speed
        elif x1 > x2:
            x1 -= self.speed
        
        # Move vertically
        if y1 < y2:
            y1 += self.speed
        elif y1 > y2:
            y1 -= self.speed
        
        # Update the enemy's position
        self.position = (x1, y1)

        if self.position == target_position:
            print("found target")
            del self.path[0]


    def draw(self, screen):
        #print(f"enemy pos is:{self.position}")
        screen.blit(self.sprite, (self.position))

    def take_damage(self):
        self.health -= 1

    def check_is_dead(self):
        if self.health <= 0:
            self.is_dead = True
            print(f"Enemy has reached end (of its life)")

    def check_has_reached_end(self):
        if len(self.path) == 0:
            self.reached_end = True
            print(f"Enemy has reached end")

    def update(self):
        self.move()
        self.check_is_dead()
        self.check_has_reached_end()

        