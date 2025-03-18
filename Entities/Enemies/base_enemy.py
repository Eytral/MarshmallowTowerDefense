from Constants import sprites, config
import copy
import pygame

class Enemy():
    def __init__(self, start_position, path, reward=5, health=10, speed=10):
        self.reward = reward
        self.health = health
        self.speed = speed
        self.position = copy.deepcopy(start_position)
        self.grid_position = (copy.deepcopy(start_position[0])//config.GRID_CELL_SIZE, copy.deepcopy(start_position[1])//config.GRID_CELL_SIZE)
        self.path = copy.deepcopy(path)
        self.is_dead = False
        self.reached_end = False
        self.sprite = sprites.ENEMY_DEFAULT_SPRITE

        self.centre_position = (self.position[0] + config.GRID_CELL_SIZE//2, self.position[1] + config.GRID_CELL_SIZE//2)

        self.prev_centre_position = copy.deepcopy(self.centre_position)
        self.prev_position = copy.deepcopy(start_position)

        self.hitbox = pygame.Rect(self.position[0], self.position[1], config.GRID_CELL_SIZE, config.GRID_CELL_SIZE)
        
    def move(self):
        for _ in range(self.speed):
            target_position = self.path[0]
            #print(f"targeting positiong: {target_position}")

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
            self.prev_position = copy.deepcopy(self.position)
            self.position = (x1, y1)
            self.centre_position = (self.position[0] + config.GRID_CELL_SIZE//2, self.position[1] + config.GRID_CELL_SIZE//2)
            self.prev_centre_position = copy.deepcopy(self.centre_position)
            self.grid_position = (x1//config.GRID_CELL_SIZE, y1//config.GRID_CELL_SIZE)
            self.hitbox = pygame.Rect(self.position[0], self.position[1], config.GRID_CELL_SIZE, config.GRID_CELL_SIZE)


            if self.position == target_position:
                #print("found target")
                del self.path[0]
                break


    def draw(self, screen):
        #print(f"enemy pos is:{self.position}")
        screen.blit(self.sprite, (self.position))

    def take_damage(self, damage):
        print(f"Enemy taken {damage} damage")
        self.health -= damage

    def check_is_dead(self):
        #print("Checking is dead")
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

        